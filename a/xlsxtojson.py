var XLSX = require("xlsx");
var fs = require("fs");

var workbook = XLSX.readFile("1.xlsx");
var sheet_name_list = workbook.SheetNames;
console.log(sheet_name_list); // getting as Sheet1

sheet_name_list.forEach(function (y) {
    var worksheet = workbook.Sheets[y];
    //getting the complete sheet
    // console.log(worksheet);

    var headers = {};
    var data = [];
    for (z in worksheet) {
        if (z[0] === "!") continue;
        //parse out the column, row, and value
        var col = z.substring(0, 1);
        // console.log(col);

        var row = parseInt(z.substring(1));
        // console.log(row);

        var value = worksheet[z].v;
        // console.log(value);

        //store header names
        if (row == 1) {
            headers[col] = value;
            // storing the header names
            continue;
        }

        if (!data[row]) data[row] = {};
        data[row][headers[col]] = value;
    }
    //drop those first two rows which are empty
    data.shift();
    data.shift();
    console.log("1. data", data);

    fs.writeFileSync("./phraseFreqs.json", JSON.stringify(data));

    /* const dataJson = JSON.stringify(data);

    var stream = fs.createWriteStream("myFile.json", { flags: "a" });

    stream.write(dataJson, function () {
        // Now the data has been written.
        console.log("g");
    }); */
});
