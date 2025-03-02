import time
import re

# Path to Game.log
LOG_FILE_PATH = r"C:\Program Files\Roberts Space Industries\StarCitizen\LIVE\Game.log"
PLAYER_NAME = "KoiNoYume7"  # Change this to your in-game name

# List of known ship manufacturers
SHIP_MANUFACTURERS = ["RSI", "DRAK", "MISC", "ANVL", "AEGS", "CRUS", "ARGO", "CNOU", "ORIG", "VNCL"]

# Improved regex to detect ships & filter out unnecessary prefixes (like SCItem_Debris)
SHIP_REGEX = re.compile(r"Entity \[.*?([A-Z]+_[A-Za-z0-9]+(?:_[A-Za-z0-9]+)*_\d+)]")

def process_log_line(line):
    """Processes a single log line to extract the player's ship name."""
    if PLAYER_NAME in line and "Entity [" in line and "m_ownerGEID" in line:
        match = SHIP_REGEX.search(line)
        if match:
            raw_ship_name = match.group(1)

            # Clean up any junk before the actual ship name (like SCItem_Debris_)
            ship_name = re.sub(r"^SCItem_Debris_\d+_", "", raw_ship_name)

            # Ensure it's a real ship (not an object)
            if any(ship_name.startswith(manufacturer) for manufacturer in SHIP_MANUFACTURERS):
                print(f"🚀 Detected Ship: {ship_name}")
            elif "_" in ship_name:
                print(f"🚀 Detected Ship: {ship_name} (No manufacturer, but valid structure)")

def tail_log():
    """Continuously reads Game.log as new lines are added."""
    with open(LOG_FILE_PATH, "r", encoding="utf-8") as file:
        file.seek(0, 2)  # Move to end of file

        while True:
            line = file.readline()
            if not line:
                time.sleep(0.1)  # Prevent high CPU usage
                continue

            process_log_line(line)

if __name__ == "__main__":
    print("🔍 Monitoring Star Citizen logs for **your** ship...")
    try:
        tail_log()
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped.")
