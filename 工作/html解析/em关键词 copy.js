const fs = require('fs');
const cheerio = require('cheerio');
const path = require("path")
const filename = 'em关键词.txt'
const words = new Set(["as necessary", "recommend", 'suggest', 'better', 'best', 'if necessary'])

const dir = "D:\\file\\doc\\"

let docArr = []

function add_doc(dir,docArr) {
    fs.readdirSync(dir).forEach(function (file) {
        const pathname = path.join(dir, file)
        // console.log(pathname)
        if (file.slice(-3) !== ".db") {
            docArr.push(pathname)
        }
    })
}

// function add_html(dir,docArr) {
//     for (let index = 0; index < dir.length; index++) {
//         const element = dir[index];
//         // console.log(element)
//         docArr.push(element)
//     }
// }


add_doc(dir,docArr)
console.log(docArr)

// for (let index = 0; index < docArr.length; index++) {
//     const element = docArr[index];
//     // console.log(element)
//     keyWord(element)
// }

// function keyWord(doc) {
//     console.log(doc)
//     // 得到文件名称
//     let fileArr = []
//     for (let index = 0; index < doc.length; index++) {
//         const element = doc[index];
//         // console.log(element)
//         fileArr.push(element)

//     console.log(fileArr)
//     // // 提取html内信息
//     // function read(input, ref_map) {
//     //     var myHtml = fs.readFileSync(input);
//     //     var $ = cheerio.load(myHtml);

//     //     // 键
//     //     var dmc = $('td[class = task]');

//     //     let tmp = input.split("\\")
//     //     let name = tmp[tmp.length - 1]

//     //     for (let index = 0; index < dmc.length; index++) {
//     //         ref_map.set(dmc[index].children[0].data,name)
//     //         }
//     // }



//     // let txtString = ""
//     // let ref_map = new Map()

//     // for (let index = 0; index < fileArr.length; index++) {
//     //     read(fileArr[index], ref_map)
//     // }
//     // // 往writeme.txt文件 写入一些内容
//     // for (let [key, value] of ref_map) {
//     //     txtString += "dmc: " + key + " ref: " + value
//     //     txtString += " \n"
//     // }

//     // fs.writeFile(filename, txtString, function (err) {
//     //     // 判断 如果有错 抛出错误 否则 打印写入成功
//     //     if (err) {
//     //         throw err;
//     //     } 
//     //     console.log('写入文件成功!')
//     // })
// }
