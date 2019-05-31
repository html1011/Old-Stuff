let fs = require("fs");
// Now that we have the data....
/*
We create a table.
Let's do this!
First group all our elements by their periods.
*/
let a = new Promise((resolve, reject) => {
    fs.readFile("PeriodicTable.csv", "utf8", (err, name) => {
        if (err) reject(err);
        let data = name.split("\n");
        data = data.map((val) => {
            return val.split(",");
        });
        // data[0] is the identifier for everything else.
        let newData = [];
        for (let i = 1; i < data.length; i++) {
            let partData = {};
            for (let ii = 0; ii < data[i].length; ii++) {
                partData[data[0][ii]] = data[i][ii];
            }
            newData.push(partData);
        }
        resolve(newData);
    });
})
a.then((values) => {
let grouped = [],
groupedVal = [],
sortBy = "Group";
//console.log(values);
let val = values.slice()
});