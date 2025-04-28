# ANNIK-A Project - Project Structure Overview (As of April 28, 2025)

## Introduction
This document summarizes the current **project structure** and **module responsibilities** of ANNIK-A during its initial development phase.

---

## High-Level Overview
- ANNIK-A is a **desktop application** designed to assist with **Star Citizen** trading and ship management.
- Built with:
  - **Electron**: For desktop application shell.
  - **React.js**: For dynamic frontend user interface.
  - **Python scripts**: For backend logic, such as log reading and cargo grid management.
- Integration between Electron/Node.js and Python is **planned** but **not finalized yet**.

---

## Directory Structure

| Path | Purpose |
|:--|:--|
| `.gitignore` | Specifies files and folders to ignore in Git versioning. |
| `dependencies.bat` | Batch script to install Node and Python dependencies (development use only). |
| `LICENSE` | Open source license placeholder. |
| `package.json` | Node.js project configuration for Electron + React frontend. |
| `README.md` | Project introduction and general usage guide. |
| `webpack.config.js` | Webpack bundling configuration for the frontend. |
| `.dist/` | Output folder for built Electron app. |
| `docs/` | Project documentation files (e.g., `LOGREADER.md`). |
| `logs/` | Contains output and parsed logs from Star Citizen and ANNIK-A scripts. |
| `public/` | Static frontend assets (HTML, CSS). |
| `Recyclebin__/` | Deprecated or old code files (manually archived, gitignored). |
| `src/` | Main source code for ANNIK-A. |
| `ui/` | Installed Electron-related files (after install/build). |

---

## Key Modules and Responsibilities

### Electron Integration
- **`src/electron/main.js`**
  - Sets up the main Electron window.
  - Loads `public/index.html` as the frontend entrypoint.
  - Currently minimal but planned for backend integration.

### Frontend (React.js)
- **`src/index.jsx`**
  - Entry point for React app.
  - Connects frontend logic with Electron shell.

### Backend (Python Scripts)
- **`src/main.py`**
  - Central controller script.
  - Manages all higher-level backend logic.
  - Delegates specific tasks to submodules (e.g., log reading).

- **`src/log_reader.py`**
  - Reads and parses live Star Citizen logs.
  - Extracts player ID, ship spawn events, hangar states, and more.

### Features
- **Config Parser (`features/configParser/cfg.py`)**
  - Loads `.cfg` configuration files into structured dictionaries.

- **3D Grid Viewer (`features/grid3DViewer/3DViewer.js`)**
  - Placeholder for 3D cargo grid visualization (under development).

- **Cargo Grid Manager (`features/grid3DViewer/cargoGridManager.py`)**
  - Calculates cargo placement and grid fitting logic.
  - Separate from 3D rendering.

- **Logger (`features/logger/logger.py`)**
  - Internal project logging system.
  - Tracks debug information and errors.

### Utilities
- **Ship Grids (`features/grid3DViewer/grids/`)**
  - JSON files representing cargo layouts for different ships.
  - (Currently only `origin100i.json` exists.)

- **Ship Stats (`src/utils/Shipstats.json`)**
  - **Deprecated**: Originally static ship data, now replaced by dynamic Star Citizen Wiki API fetch.

---

## Development Workflow
1. Install Node.js and Python dependencies via `dependencies.bat`.
2. Start Electron + React frontend.
3. Backend Python scripts run separately or via Electron-Node integration (planned).
4. Logs processed and exported to `/logs/`.
5. Future: Full integration of Python backend with Electron frontend.

---

## Future Plans
- Integrate Python backend live into Electron frontend.
- Expand grid database with more Star Citizen ships.
- Implement dynamic cargo grid 3D viewer.
- Introduce advanced error handling with `logger.py`.
- Open source project for public contributions (e.g., ship grids).

---

# End of Document

This documentation will be updated as ANNIK-A evolves further!

