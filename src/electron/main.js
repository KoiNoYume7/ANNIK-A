const { app, BrowserWindow } = require('electron');
const path = require('path');
const { spawn } = require('child_process'); // ← Add this line

let mainWindow;

function createWindow() {
  app.whenReady().then(() => {
    // 🔥 Spawn Python backend
    const pythonProcess = spawn('python', [path.join(__dirname, '..', 'main.py')]);
    
    // Log Python output
    pythonProcess.stdout.on('data', (data) => {
      console.log(`[PYTHON] ${data.toString()}`);
    });

    pythonProcess.stderr.on('data', (data) => {
      console.error(`[PYTHON ERROR] ${data.toString()}`);
    });

    pythonProcess.on('close', (code) => {
      console.log(`[PYTHON] exited with code ${code}`);
    });

    // 🪟 Create frontend window
    mainWindow = new BrowserWindow({
      width: 800,
      height: 600,
      webPreferences: {
        preload: path.join(__dirname, 'preload.js'),
        contextIsolation: true,
        nodeIntegration: false,
        enableRemoteModule: false,
      },
    });

    void mainWindow.loadURL(!app.isPackaged
      ? "http://localhost:8080"
      : `file://${path.join(__dirname, "dist", "index.html")}`);
  });
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
    mainWindow = null;
  }
});
