import time
import re

LOG_FILE_PATH = r"C:\\Program Files\\Roberts Space Industries\\StarCitizen\\LIVE\\Game.log"
SHOW_ADDITIONAL_INFO = True
PLAYER_NAME = "KoiNoYume7"  # Case sensitive player name

player_id = None
player_name = None
active_ship = None
ship_spawned = False
current_hangar_state = None

regex_player_login = re.compile(r"AccountLoginCharacterStatus_Character.*?geid (\\d+).*?name (\\w+)")
regex_entity_spawn = re.compile(r"EntitySpawnBatch.*?Data/objectcontainers/ships/([a-z]+)/([a-zA-Z0-9_]+)")
regex_hangar_state = re.compile(r"LoadingPlatformManager.*?Platform state changed to (\\w+)")
regex_comms_player_id = re.compile(rf"{PLAYER_NAME} \\\\[(\\\\d+)\\\\]")

def update_variable(name, value):
    if SHOW_ADDITIONAL_INFO:
        print(f"[UPDATE] {name} -> {value}", flush=True)

def process_log_line(line):
    global player_id, player_name, active_ship, ship_spawned, current_hangar_state

    # Capture player ID from login
    if player_id is None:
        match = regex_player_login.search(line)
        if match:
            player_id = match.group(1)
            player_name = match.group(2)
            print(f"[INFO] Captured Player ID from login: {player_id} (Name: {player_name})", flush=True)
            if SHOW_ADDITIONAL_INFO:
                print(f"[RAW] {line.strip()}", flush=True)
            return

    # Capture player ID from comms line
    if player_id is None and PLAYER_NAME in line:
        match = regex_comms_player_id.search(line)
        if match:
            player_id = match.group(1)
            print(f"[INFO] Captured Player ID from comms: {player_id}", flush=True)
            if SHOW_ADDITIONAL_INFO:
                print(f"[RAW] {line.strip()}", flush=True)
            return

    if "EntitySpawnBatch" in line:
        match = regex_entity_spawn.search(line)
        if match and not ship_spawned:
            manufacturer = match.group(1).upper()
            ship_name = match.group(2)
            active_ship = f"{manufacturer}_{ship_name}"
            ship_spawned = True
            print(f"[EVENT] Ship spawn detected: {active_ship}", flush=True)
            update_variable("active_ship", active_ship)
            update_variable("ship_spawned", ship_spawned)
            if SHOW_ADDITIONAL_INFO:
                print(f"[RAW] {line.strip()}", flush=True)
            return

    if "LoadingPlatformManager" in line:
        match = regex_hangar_state.search(line)
        if match:
            new_state = match.group(1)
            current_hangar_state = new_state
            print(f"[EVENT] Hangar platform changed state: {current_hangar_state}", flush=True)
            update_variable("current_hangar_state", current_hangar_state)

            if current_hangar_state == "LoweringPlatform":
                print("[INFO] Platform lowering - Ship incoming", flush=True)
            elif current_hangar_state == "ClosingLoadingGate":
                print("[INFO] Hangar door closing - Storing ship", flush=True)
            elif current_hangar_state == "ClosedIdle":
                if active_ship:
                    print(f"[SUCCESS] {active_ship} stored safely (Hangar closed)", flush=True)
                    active_ship = None
                    ship_spawned = False
                    update_variable("active_ship", active_ship)
                    update_variable("ship_spawned", ship_spawned)
                else:
                    print("[WARNING] Hangar closed but no active ship detected.", flush=True)
            if SHOW_ADDITIONAL_INFO:
                print(f"[RAW] {line.strip()}", flush=True)
            return

def tail_log():
    with open(LOG_FILE_PATH, "r", encoding="utf-8") as file:
        file.seek(0, 2)

        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)
                continue
            process_log_line(line)

if __name__ == "__main__":
    print("[ANNIK-A] Log Reader Initialized.", flush=True)

    try:
        tail_log()
    except KeyboardInterrupt:
        print("\nMonitoring stopped.", flush=True)
