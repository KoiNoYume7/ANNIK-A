import json
import os
import shutil

DEFAULT_SETTINGS_FILE = "settings.default.json"
USER_SETTINGS_FILE = "settings.json"

def load_settings():
    if not os.path.exists(USER_SETTINGS_FILE):
        print("[SETTINGS] settings.json not found. Creating from default.", flush=True)
        if os.path.exists(DEFAULT_SETTINGS_FILE):
            shutil.copy(DEFAULT_SETTINGS_FILE, USER_SETTINGS_FILE)
            print("[SETTINGS] Default settings copied to settings.json.", flush=True)
        else:
            raise FileNotFoundError("Default settings file missing!")

    try:
        with open(USER_SETTINGS_FILE, "r", encoding="utf-8") as f:
            settings = json.load(f)
            print("[SETTINGS] Loaded user settings successfully.", flush=True)
            return settings
    except Exception as e:
        print(f"[ERROR] Failed to load user settings: {e}", flush=True)
        raise e

def save_settings(settings):
    try:
        with open(USER_SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump(settings, f, indent=4)
        print("[SETTINGS] settings.json saved successfully.", flush=True)
    except Exception as e:
        print(f"[ERROR] Failed to save user settings: {e}", flush=True)

# Allow standalone quick test
if __name__ == "__main__":
    settings = load_settings()
    print(settings)
