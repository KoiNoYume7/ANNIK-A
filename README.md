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

> The name "ANNIK-A" has been inspired by a person who helped me actually work on Projects like this. In honor to this person, it has become the name of this Project.

---

## Project Vision

ANNIK-A aims to be the ultimate Star Citizen utility, combining:
- Assisting in cargo logic with **optional** automatic game.log tracker to save time and increase accuracy.
- **Up-to-date** information using **Star Citizen Wiki API**
- Advanced **3D cargo grid visualizer**
- Smart logic for **manual vs auto loading decisions**
- **Planned** profit and trip logging
- Future support for **mining/refinery optimizations**

The goal: to help new and experienced players manage cargo, save time, increase profit margins, and turn chaos into clean logistics. 

## Core Features

### ✅ Implemented
- Basic player and ship tracking from Star Citizen `game.log` for optional automatisation
- Config parser for internal modular settings
- Log reading and event handling foundations (`main.py` + `log_reader.py`)

### 🚧 In Development
- 3D Cargo Grid Viewer with smart box fitting
- Cargo grid calculator (fitting cargo efficiently into ships)
- UI groundwork with Electron + React and website (for both dekstop app or website access)
- Python ↔ Electron integration (backend-frontend connection)

### 🌱 Planned
- Mining mode: Predict refinery output and container fitting
- For visualization and logging
- Multi-crew logic

---

## 🛠️ Technologies Used
- Python (core logic, log parsing, cargo calculations)
- React + Electron (frontend and desktop app shell)
- Webpack (build tooling)
- JSON for ship cargo grid layouts (for developing reasons, not yet optimized)
- Star Citizen Wiki API for live data

## 📦 Getting Started

### 1️⃣ Installation

#### Dependencies
Make sure you have the following installed:
- **Python 3.1x**
- **Node.js & npm**

Install Python dependencies:
```bash
pip install -r requirements.txt 
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
Path and user handle must be edited manually for now!

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

## 🌐 APIs, Collaborations and Partnerships

### APIs Used
- https://starcitizen.tools (Star Citizen Wiki)

### Collaborations
- @Araytar (backend integration)


## 📝 Last Words

Special thanks to @Araytar for being a beast with backend logic, ChatGPT for writing documentations and the Star Citizen community for providing open APIs (love yall ^^).

ANNIK-A is open source and welcomes future contributions, especially maintaining everything up-to-date, because I am lazy.
