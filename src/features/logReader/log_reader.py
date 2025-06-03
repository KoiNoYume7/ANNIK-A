import time
import re
import json
from pathlib import Path

class LogReader:
    def __init__(self, log_file_path, player_name, show_additional_info=True):
        self.log_file_path = log_file_path
        self.player_name = player_name
        self.show_additional_info = show_additional_info

        # Internal state
        self.player_id = None
        self.active_ship_data_path = Path("active_ship.json")
        self.ship_registry_path = Path("ship_ids.json")
        self.active_ship = None

        # Regex
        self.regex_player_login = re.compile(r"AccountLoginCharacterStatus_Character.*?geid (\d+).*?name (\w+)")
        self.regex_comms_player_id = re.compile(rf"{self.player_name} \[(\d+)\]")
        self.regex_set_driver = re.compile(r"SetDriver: Local client node \[(\d+)\] requesting control token for '(.+?)' \[(\d+)\]")
        self.regex_clear_driver = re.compile(r"ClearDriver: Local client node \[(\d+)\] releasing control token for '(.+?)' \[(\d+)\]")
        self.regex_hangar_state = re.compile(r"LoadingPlatformManager.*?Platform state changed to (\w+)")

        self._running = False

    def _update_active_ship(self, ship_id, ship_name, in_seat, active):
        data = {
            "player_id": self.player_id,
            "ship_id": ship_id,
            "ship_name": ship_name,
            "in_seat": in_seat,
            "active": active
        }
        with open(self.active_ship_data_path, "w") as f:
            json.dump(data, f, indent=4)
        if self.show_additional_info:
            print(f"[UPDATE] Active ship updated: {data}", flush=True)

    def _load_ship_registry(self):
        if self.ship_registry_path.exists():
            with open(self.ship_registry_path, "r") as f:
                return json.load(f)
        return {}

    def _save_ship_registry(self, registry):
        with open(self.ship_registry_path, "w") as f:
            json.dump(registry, f, indent=4)

    def _process_log_line(self, line):
        if self.player_id is None:
            match = self.regex_player_login.search(line)
            if match:
                self.player_id = match.group(1)
                print(f"[INFO] Player ID captured from login: {self.player_id}", flush=True)
                return
            match = self.regex_comms_player_id.search(line)
            if match:
                self.player_id = match.group(1)
                print(f"[INFO] Player ID captured from comms: {self.player_id}", flush=True)
                return

        # Enter seat
        match = self.regex_set_driver.search(line)
        if match and match.group(1) == self.player_id:
            full_ship_name = match.group(2)
            ship_id = match.group(3)
            registry = self._load_ship_registry()
            if ship_id not in registry:
                registry[ship_id] = full_ship_name
                self._save_ship_registry(registry)
                print(f"[NEW] Registered new ship: {full_ship_name} -> {ship_id}", flush=True)
            self._update_active_ship(ship_id, registry[ship_id], in_seat=True, active=True)
            return

        # Exit seat
        match = self.regex_clear_driver.search(line)
        if match and match.group(1) == self.player_id:
            ship_id = match.group(3)
            registry = self._load_ship_registry()
            if ship_id in registry:
                self._update_active_ship(ship_id, registry[ship_id], in_seat=False, active=True)
            return

        # Hangar platform change
        match = self.regex_hangar_state.search(line)
        if match:
            state = match.group(1)
            if state == "ClosedIdle":
                # Ship has been stored
                if self.active_ship_data_path.exists():
                    with open(self.active_ship_data_path, "r") as f:
                        data = json.load(f)
                    data["active"] = False
                    data["in_seat"] = False
                    with open(self.active_ship_data_path, "w") as f:
                        json.dump(data, f, indent=4)
                    print(f"[INFO] Ship stored: {data['ship_name']} (Hangar ClosedIdle)", flush=True)
            return

    def start(self):
        print("[ANNIK-A] Unified Log Reader Started.", flush=True)
        self._running = True
        try:
            with open(self.log_file_path, "r", encoding="utf-8") as file:
                file.seek(0, 2)
                while self._running:
                    line = file.readline()
                    if not line:
                        time.sleep(0.1)
                        continue
                    self._process_log_line(line)
        except FileNotFoundError:
            print(f"[ERROR] Log file not found: {self.log_file_path}", flush=True)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        self._running = False
        print("[ANNIK-A] Log Reader Stopped.", flush=True)

if __name__ == "__main__":
    reader = LogReader(
        log_file_path=r"C:\\Program Files\\Roberts Space Industries\\StarCitizen\\LIVE\\Game.log",
        player_name="KoiNoYume7",
        show_additional_info=True
    )
    reader.start()
