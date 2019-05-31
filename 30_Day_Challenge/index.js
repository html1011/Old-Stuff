const net = require("net");
let ourClients = [];
server = net.createServer((socket) => {
    // console.log(socket);
    socket.on("end", () => {
        console.log("Someone disconnected....");
    })
    socket.write("Yo yo yo!");
    socket.pipe(socket);
}).on("error", (err) => {
    if(err.code == "EADDRINUSE") {
        console.log("Gulp. Someone else is using this. Let's try again....");
        setTimeout(() => {
            server.close();
            server.listen();
        }, 1000);
    } else {
        throw err;
    }
});

server.on("connection", (someone) => {
    ourClients.push({});
    someone.write("Wassup?\n");
    someone.write("Please enter your username: ");
    console.log(ourClients.length + " people are connected.");
    someone.on("data", (data) => {
        console.log(data.toString());
    })
});

server.listen({
    host: "localhost",
    port: 3030,
    exclusive: false
}, () => {
    console.log(`Opened a server on `, server.address().address == "::" ? "localhost:" + server.address().port : server.address().address + ":" + server.address().port);
})
// const http = require("http")
// http.createServer((req, res) => {
//     console.log(req);
//     res.write("Heeeeello there!");
//     res.close();
// }).listen(3030, "localhost")