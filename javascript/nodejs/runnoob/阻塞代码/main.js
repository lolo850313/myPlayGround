var fs = require("fs")

// var data = fs.readFileSync('input.txt')

// console.log(data.toString())

fs.readFile('input.txt', function (err, data) {
    if(err){
        console.error(err);
        return 
    }
    console.log(data);
})

console.log("end");