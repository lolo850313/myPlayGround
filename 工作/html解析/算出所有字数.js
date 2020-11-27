const fs = require('fs');
const cheerio = require('cheerio');
const Excel = require('exceljs')
const path = require("path");
const { count } = require('console');
const { stringify } = require('querystring');
const filename = 'C:\\winGit\\工作\\gek9250_sum.txt'

// const dir = "D:\\工作文档\\2019.11 EM\\doc\\gek112091\\"
const dir = "D:\\工作文档\\2019.04.SPM\\doc\\gek9250\\"

function travel(dir, callback) {
    fs.readdirSync(dir).forEach(function (file) {
        let pathname = path.join(dir, file);

        if (fs.statSync(pathname).isDirectory()) {
            travel(pathname, callback);
        } else {
            callback(pathname);
        }
    });
}

// 提取html内信息
function read(input, ref_map) {
    let myHtml = fs.readFileSync(input);
    let $ = cheerio.load(myHtml);

    let c = $.text().split(" ").length;
    let k = input.split("\\").pop()
    ref_map.set(k, c)
    total += c
}



// 得到文件名称
let  fileArr = []
travel(dir, function (pathname) {
    fileArr.push(pathname);
});

let total = 0
let ref_map = new Map()

for (let index = 0; index < fileArr.length; index++) {
    read(fileArr[index], ref_map) 
}


let txtString = "total: " + total + " \n"
for (let [key, value] of ref_map) {
    txtString += "dmc: " + key + " count: " + (value) + " \n"
}

fs.writeFile(filename, txtString, function (err) {
    // 判断 如果有错 抛出错误 否则 打印写入成功
    if (err) {
        throw err;
    } 
    console.log('写入文件成功!')
})


