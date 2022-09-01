var fs = require('fs');
const results = fs.readdirSync("./", { withFileTypes: true });
results.forEach(function(result) {
   const boolean = result.isDirectory()
    if(boolean){
        var files = fs.readdirSync('./'+result.name);
        var size = Object.keys(files).length
        for(var i = 0; i < size; i++){
            console.log(files[i])
        }
       console.log(size)
    }
});
