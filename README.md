# ANNIK-A
> "From cargo to credits, ANNIK-A has your back."

**ANNIK-A**
- **A**nalytics
- **N**avigation
- **N**etwork
- **I**nterface
- **K**nowledge
- **A**ssistant

is a powerful and extensible Star Citizen companion tool designed to bring maximum efficiency, clarity, and control to the cargo experience within the 'verse.

The name "ANNIK-A" is inspired by a real person who helped spark the concept.

---

## 🚀 Project Vision

ANNIK-A aims to be the ultimate Star Citizen utility, combining:
- Real-time **ship activity tracking**
- **Up-to-date** information for everything thanks to **APIs** (see @**APIs, Collaborations and Partnerships**)
- Advanced **3D cargo grid visualizer**
- Smart logic for **manual vs auto loading decisions**
- **Trip and profit logging** based on game.log parsing
- Planned future support for **mining/refinery optimizations**

The goal: to save time, increase profit margins, and turn chaos into clean logistics.

---

## 🧩 Core Features

### ✅ Implemented
- Track pulled ships and ship destruction from Star Citizen's `game.log`
- Calculate trip durations & inferred profit margins
- Config parser & internal logic foundation

### 🚧 In Development
- 3D Cargo Grid Viewer with smart box fitting
- Efficient cargo packing (reduce number of boxes needed to load)
- Basic UI logic groundwork (Electron + React)

### 🌱 Planned
- Mining mode: Assist refinery output prediction to avoid oversized box errors
- Station-specific loading logic (auto/manual time analysis)
- Profit-per-trip visualization
- API integrations with:
  - Star Citizen Wiki
  - uex.corp (if available)
  - sc-trade.tools (if accessible)
  - regolith.rocks (non-conflicting)

---

## 🛠️ Technologies Used
- Python (core logic, log parsing)
- React + Electron (UI/frontend layer)
- Webpack (frontend build tool)
- JSON cargo grid mapping per ship model
- Optimized log reading for your ship

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

> Make sure Star Citizen is running and logs are updating in real-time.

## 🗂️ Project File Structure

```
ANNIK-A
|   .gitignore
|   dependencies.bat
|   LICENSE
|   package.json
|   README.md
|   webpack.config.js
|   
+---public
|       index.css
|       index.html
|
\---src
    |   index.jsx
    |   log_reader.py
    |   main.py
    |
    +---electron
    |       main.js
    |
    \---features
        +---configParser
        |       cfg.py
        |
        +---grid3DViewer
        |   |   3DViewer.js
        |   |   cargoGridManager.py
        |   \---grids
        |           origin100i.json
        |
        \---logger
                logger.py
```

## 🌐 APIs, Collaborations and Partnerships

### APIs Used
- https://starcitizen.tools

### Collaborations
- @Araytar

### Partnerships
- none (yet?)

---

## 📝 Last Words
Thanks to my dude Araytar for helping me, ChatGPT who wrote this README because Akira was too lazy, and the community for providing APIs (those are lifesavers).

