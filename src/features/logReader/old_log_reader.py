import time
import re

class LogReader:
    def __init__(self, log_file_path, player_name, show_additional_info=True):
        self.log_file_path = log_file_path
        self.player_name = player_name
        self.show_additional_info = show_additional_info

        # Internal variables
        self.player_id = None
        self.active_ship = None
        self.ship_spawned = False
        self.current_hangar_state = None

        # Precompiled regex
        self.regex_player_login = re.compile(r"AccountLoginCharacterStatus_Character.*?geid (\d+).*?name (\w+)")
        self.regex_entity_spawn = re.compile(r"EntitySpawnBatch.*?Data/objectcontainers/ships/([a-z]+)/([a-zA-Z0-9_]+)")
        self.regex_hangar_state = re.compile(r"LoadingPlatformManager.*?Platform state changed to (\w+)")
        self.regex_comms_player_id = re.compile(rf"{self.player_name} \[(\d+)\]")

        # Control flag
        self._running = False

    def _update_variable(self, name, value):
        if self.show_additional_info:
            print(f"[UPDATE] {name} -> {value}", flush=True)

    def _process_log_line(self, line):
        # Capture player ID from login
        if self.player_id is None:
            match = self.regex_player_login.search(line)
            if match:
                self.player_id = match.group(1)
                print(f"[INFO] Captured Player ID from login: {self.player_id}", flush=True)
                if self.show_additional_info:
                    print(f"[RAW] {line.strip()}", flush=True)
                return

        # Capture player ID from comms
        if self.player_id is None and self.player_name in line:
            match = self.regex_comms_player_id.search(line)
            if match:
                self.player_id = match.group(1)
                print(f"[INFO] Captured Player ID from comms: {self.player_id}", flush=True)
                if self.show_additional_info:
                    print(f"[RAW] {line.strip()}", flush=True)
                return

        if "EntitySpawnBatch" in line:
            match = self.regex_entity_spawn.search(line)
            if match and not self.ship_spawned:
                manufacturer = match.group(1).upper()
                ship_name = match.group(2)
                self.active_ship = f"{manufacturer}_{ship_name}"
                self.ship_spawned = True
                print(f"[EVENT] Ship spawn detected: {self.active_ship}", flush=True)
                self._update_variable("active_ship", self.active_ship)
                self._update_variable("ship_spawned", self.ship_spawned)
                if self.show_additional_info:
                    print(f"[RAW] {line.strip()}", flush=True)
                return

        if "LoadingPlatformManager" in line:
            match = self.regex_hangar_state.search(line)
            if match:
                new_state = match.group(1)
                self.current_hangar_state = new_state
                print(f"[EVENT] Hangar platform changed state: {self.current_hangar_state}", flush=True)
                self._update_variable("current_hangar_state", self.current_hangar_state)

                if self.current_hangar_state == "LoweringPlatform":
                    print("[INFO] Platform lowering - Ship incoming", flush=True)
                elif self.current_hangar_state == "ClosingLoadingGate":
                    print("[INFO] Hangar door closing - Storing ship", flush=True)
                elif self.current_hangar_state == "ClosedIdle":
                    if self.active_ship:
                        print(f"[SUCCESS] {self.active_ship} stored safely (Hangar closed)", flush=True)
                        self.active_ship = None
                        self.ship_spawned = False
                        self._update_variable("active_ship", self.active_ship)
                        self._update_variable("ship_spawned", self.ship_spawned)
                    else:
                        print("[WARNING] Hangar closed but no active ship detected.", flush=True)
                if self.show_additional_info:
                    print(f"[RAW] {line.strip()}", flush=True)
                return

    def start(self):
        print("[ANNIK-A] Log Reader Started.", flush=True)
        self._running = True
        try:
            with open(self.log_file_path, "r", encoding="utf-8") as file:
                file.seek(0, 2)  # Go to the end of file
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

# Allow standalone running
if __name__ == "__main__":
    reader = LogReader(
        log_file_path=r"C:\\Program Files\\Roberts Space Industries\\StarCitizen\\LIVE\\Game.log",
        player_name="KoiNoYume7",
        show_additional_info=False
    )
    reader.start()
