import time
import re
import sys

LOG_FILE_PATH = r"C:\Program Files\Roberts Space Industries\StarCitizen\LIVE\Game.log"
PLAYER_NAME = "KoiNoYume7"  # Change this to your in-game name

DEBUG = False  # Default is Off

SHIP_MANUFACTURERS = ["AEGS", "ANVL", "XNAA", "ARGO", "CNOU", "CRUS", "DRAK", "ESPR", "GAMA", "KRIG", "MRAI", "ORIG", "RSI"]

# Exclude known junk prefixes (things that aren't ships)
EXCLUDED_PREFIXES = ["FTUE_", "SOC_", "StreamingSOC_", "TagPoint_", "Room_", "Elevator_", "Hangar_", "Transit_", "SpawnCloset_"]

# Improved regex to detect ships & filter out unnecessary prefixes (like SCItem_Debris)
SHIP_REGEX = re.compile(r"Entity \[.*?([A-Z]+_[A-Za-z0-9]+(?:_[A-Za-z0-9]+)*_\d+)]")

def process_log_line(line, line_number):
    """Processes a single log line to extract the player's ship name and sends it to Electron."""
    if PLAYER_NAME in line and "Entity [" in line and "m_ownerGEID" in line:
        match = SHIP_REGEX.search(line)
        if match:
            raw_ship_name = match.group(1)

            # Clean up any junk before the actual ship name (like SCItem_Debris_)
            ship_name = re.sub(r"^SCItem_Debris_\d+_", "", raw_ship_name)

            # Ignore non-ship objects using the excluded prefixes
            if any(ship_name.startswith(prefix) for prefix in EXCLUDED_PREFIXES):
                return  # Skip this detection, it's not a ship

            # Ensure it's a real ship (not an object)
            if any(ship_name.startswith(manufacturer) for manufacturer in SHIP_MANUFACTURERS):
                output = f"Detected Ship: {ship_name}"
            elif "_" in ship_name:
                output = f"Detected Ship: {ship_name} (No manufacturer, but valid structure)"
            else:
                return  # Skip invalid detections

            # Print to stdout & flush to send immediately to Electron
            print(output, flush=True)

def tail_log():
    """Continuously reads Game.log as new lines are added, with full line output if debug mode is enabled."""
    with open(LOG_FILE_PATH, "r", encoding="utf-8") as file:
        file.seek(0, 2)  # Move to end of file
        line_number = sum(1 for _ in open(LOG_FILE_PATH, "r", encoding="utf-8"))  # Get initial line count

        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)  # Prevent high CPU usage
                continue

            line_number += 1
            process_log_line(line, line_number)

if __name__ == "__main__":
    print("Monitoring Star Citizen logs for your ship...", flush=True)
    if DEBUG:
        print("Debug Mode: ON (Showing full log entries)", flush=True)
    else:
        print("Debug Mode: OFF (Showing only detected ships)", flush=True)

    try:
        tail_log()
    except KeyboardInterrupt:
        print("\nMonitoring stopped.", flush=True)
