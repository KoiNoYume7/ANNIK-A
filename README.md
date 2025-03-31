# ANNIK-A (Automated Network & Interface Kernel)

## 🚀 Overview
**ANNIK-A** (or **ANI-A** for short) is a real-time external **ship detection and data overlay system** for **Star Citizen**. It extracts live data from log files, detects the player's currently piloted ship, and fetches relevant stats for display on an external device or second monitor.

## 🌟 Features
- **🔍 Log File Parsing** → Reads and processes Star Citizen log files in real-time.
- **🚢 Ship Detection** → Identifies the player's currently piloted ship.
- **📊 Data Overlay** → Displays ship stats, cargo capacity, and other useful information.
- **🌐 API Integration** → Fetches ship details dynamically from the **Star Citizen Wiki API**.
- **📡 Modular & Expandable** → Designed as a multi-use framework for future integrations.

## 📂 Repository Structure
```
ANNIK-A/
│── src/         # Main scripts for log parsing and data processing
│── logs/        # Test log files (for debugging purposes)
│── ui/          # Electron-based graphical interface
│── docs/        # Documentation & API references
│── README.md    # Project documentation
│── package.json # Electron dependencies
```

## 🔧 Getting Started
### **1️⃣ Installation**
#### **Dependencies**
Ensure you have the following installed:
- **Python 3.x**
- **Node.js & npm** (for the Electron UI)

Then, install required Python dependencies:
```bash
pip install watchdog pandas requests
```

Install Node dependencies for the UI:
```bash
cd electron
npm install
```

### **2️⃣ Running ANNIK-A**
#### **Run the Python Log Monitor**
```bash
python src/log_reader.py
```
#### **Start the Electron UI**
```bash
cd electron
npm start
```

## 🎧 Notes
- **Make sure Star Citizen is running**, as log files update in real-time.
- **Configure `log_reader.py` with your in-game player name** for accurate detection.
- The UI will automatically update as new ships are detected.

## ⚠ Roadmap
- **✅ Log file parsing** (Extract ship data in real-time)
- **🛠️ API integration** (Fetch ship details dynamically)
- **🔬 Advanced tracking** (Landing gear, docked status, etc.)
- **💡 Data display overlay** (Show stats externally)

## 🐝 License
MIT License (Open Source & Free to Modify)