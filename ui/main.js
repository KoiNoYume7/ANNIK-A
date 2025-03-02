const { app, BrowserWindow } = require('electron');
const { spawn } = require('child_process');
const path = require('path');

let mainWindow;
let pythonProcess;

app.whenReady().then(() => {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        }
    });

    mainWindow.loadFile("index.html");
    startPythonProcess();
});

function startPythonProcess() {
    const pythonPath = "python"; // Change to full path if needed
    const scriptPath = path.join(__dirname, "../src/log_reader.py");

    console.log("🚀 Starting Python process...");
    console.log("📂 Python Path:", pythonPath);
    console.log("📜 Script Path:", scriptPath);

    pythonProcess = spawn(pythonPath, [scriptPath], { shell: true });

    pythonProcess.stdout.on('data', (data) => {
        const message = data.toString().trim();
        console.log("🐍 Python Output:", message);
        if (mainWindow) {
            mainWindow.webContents.send('update-data', message);
        } else {
            console.error("❌ Electron window not ready, skipping UI update.");
        }
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error("❌ Python Error:", data.toString());
    });

    pythonProcess.on('close', (code) => {
        console.log(`⚠️ Python script exited with code ${code}`);
    });
}

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        if (pythonProcess) pythonProcess.kill();
        app.quit();
    }
});
