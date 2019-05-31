const { app, BrowserWindow } = require('electron')
let createWindow = () => {
    let win = new BrowserWindow({ show: true })
    // win.once('ready-to-show', () => {
    // win.show()
    // })
    win.loadFile("./index.html");
};
app.on("ready", createWindow)