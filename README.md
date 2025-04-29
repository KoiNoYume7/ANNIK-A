# ANNIK-A - Star Citizen Cargo Assistant
> "From cargo to credits, ANNIK-A has your back."

**ANNIK-A**
- **A**nalytics
- **N**avigation
- **N**etwork
- **I**nterface
- **K**nowledge
- **A**ssistant

is a powerful and extensible **cargo-focused companion tool for *Star Citizen***, designed to maximize cargo efficiency, track your ship activities, and optimize trading operations in the 'verse.

Whether you're hauling freight across systems, planning mining runs, or trying to squeeze every SCU into your ship, ANNIK-A helps you **plan smarter, load faster, and profit more**.

The name "ANNIK-A" is inspired by a real person who helped spark the concept.

---

## 🚀 Project Vision

ANNIK-A aims to be the ultimate Star Citizen utility, combining:
- Real-time **ship activity tracking**
- **Up-to-date** information using **Star Citizen Wiki API**
- Advanced **3D cargo grid visualizer**
- Smart logic for **manual vs auto loading decisions**
- **Planned** profit and trip logging
- Future support for **mining/refinery optimizations**

The goal: to save time, increase profit margins, and turn chaos into clean logistics.

---

## 🤩 Core Features

### ✅ Implemented
- Basic player and ship tracking from Star Citizen `game.log`
- Ship spawn and hangar state monitoring
- Config parser for internal modular settings
- Log reading and event handling foundations (`main.py` + `log_reader.py`)

### 🚧 In Development
- 3D Cargo Grid Viewer with smart box fitting
- Cargo grid calculator (fitting cargo efficiently into ships)
- UI groundwork with Electron + React
- Python ↔ Electron integration (backend-frontend connection)

### 🌱 Planned
- Mining mode: Predict refinery output and container fitting
- Station-specific loading logic (analyzing best loading method per station)
- Profit-per-trip visualization and logging
- Extended API integrations:
  - Star Citizen Wiki
  - uex.corp (if accessible)
  - sc-trade.tools (pending)
  - regolith.rocks (non-conflicting)

---

## 🛠️ Technologies Used
- Python (core logic, log parsing, cargo calculations)
- React + Electron (frontend and desktop app shell)
- Webpack (build tooling)
- JSON for ship cargo grid layouts
- Star Citizen Wiki API for live data

---

## 📦 Getting Started

### 1️⃣ Installation

#### Dependencies
Make sure you have the following installed:
- **Python 3.1x**
- **Node.js & npm**

Install Python dependencies:
```bash
pip install watchdog requests
```

Install Node dependencies:
```bash
npm install
```

### 2️⃣ Running ANNIK-A (Dev Mode)

Run ANNIK-A in development mode (React + Electron):
```bash
npm run dev
```

> Make sure Star Citizen is running and logs are updating live.

---

## 📂 Project File Structure (as of April 28, 2025)

```
ANNIK-A
|   .gitignore
|   dependencies.bat
|   LICENSE
|   package.json
|   README.md
|   webpack.config.js
|
+---!documentation!
|       LOGREADER.md
|       PROJECTSTRUCTURE.md
|
+---.dist
+---logs
+---public
|       index.css
|       index.html
|
+---src
|   |   index.jsx
|   |   log_reader.py
|   |   main.py
|   |
|   +---electron
|   |       main.js
|   |
|   +---features
|   |   +---configParser
|   |   |       cfg.py
|   |   +---grid3DViewer
|   |   |   |   3DViewer.js
|   |   |   |   cargoGridManager.py
|   |   |   \---grids
|   |   |           origin100i.json
|   |   \---logger
|   |           logger.py
|   |
|   \---utils
|           (ship stats deprecated)
|
\---ui
    |   package-lock.json
    |   (electron installed files)
```

---

## 🌐 APIs, Collaborations and Partnerships

### APIs Used
- https://starcitizen.tools (Star Citizen Wiki)

### Collaborations
- @Araytar (backend integration)

### Partnerships
- none yet (but open to future partnerships)

---

## 📝 Last Words

Special thanks to @Araytar for being a beast with backend logic, ChatGPT for helping structure documentation, and the Star Citizen community for providing open APIs.

ANNIK-A is open source and welcomes future contributions, especially cargo grid layouts for all ships!

> "From cargo to credits, we got your back."

---