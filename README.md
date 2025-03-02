# ANNIK-A (Automated Network & Interface Kernel)

## 🚀 Overview
**ANNIK-A** (or **ANI-A** for short) is a real-time external **ship detection and data overlay system** for **Star Citizen**. It extracts live data from log files, detects the player's currently piloted ship, and fetches relevant stats (such as cargo capacity) for display on an external device or second monitor.

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
│── docs/        # Documentation & API references
│── README.md    # Project documentation
```

## 🔧 Getting Started
### **1️⃣ Installation**
Ensure you have **Python 3.x** installed. Then, install the necessary dependencies:
```bash
pip install watchdog pandas requests
```

### **2️⃣ Running ANNIK-A**
To start monitoring logs, run:
```bash
python src/main.py
```

## 🚧 Roadmap
- **✅ Log file parsing** (Extract ship data in real-time)
- **🚧 API integration** (Fetch ship details dynamically)
- **🔜 Data display overlay** (Show stats externally)

## 📜 License
MIT License (Open Source & Free to Modify)

