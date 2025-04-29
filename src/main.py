from settings import load_settings
from features.logReader.log_reader import LogReader

def main():
    # Load settings
    settings = load_settings()

    # Check selected mode
    mode = settings.get("mode", "electron").lower()

    if mode == "electron":
        print("[ANNIK-A] Starting in Electron Mode.", flush=True)
        # Start the log reader
        reader = LogReader(
            log_file_path=settings.get("log_file_path"),
            player_name=settings.get("player_name"),
            show_additional_info=True
        )
        try:
            reader.start()
        except KeyboardInterrupt:
            reader.stop()

    elif mode == "web":
        print("[ANNIK-A] Starting in Web Mode.", flush=True)
        print("[ANNIK-A] No backend log reading. Frontend UI only.", flush=True)
        # TODO: Connect frontend server if needed (later)

    else:
        print(f"[ERROR] Unknown mode '{mode}'. Check your settings.json.", flush=True)

if __name__ == "__main__":
    main()
