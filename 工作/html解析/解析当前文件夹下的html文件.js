const fs = require('fs');
const cheerio = require('cheerio');
const Excel = require('exceljs')
const path = require("path")
const filename = 'C:\\winGit\\工作\\res.txt'

// const dir = "D:\\工作文档\\2019.11 EM\\doc\\gek112091\\"
const dir = "D:\\工作文档\\2019.04.SPM\\doc\\gek9250\\"

function travel(dir, callback) {
    fs.readdirSync(dir).forEach(function (file) {
        var pathname = path.join(dir, file);

        if (fs.statSync(pathname).isDirectory()) {
            travel(pathname, callback);
        } else {
            callback(pathname);
        }
    });
}

// 得到文件名称
var fileArr = []
travel(dir, function (pathname) {
    fileArr.push(pathname);
});

// 提取html内信息
function read(input, ref_map) {
    var myHtml = fs.readFileSync(input);
    var $ = cheerio.load(myHtml);

    // 键
    var dmc = $('td[class = task]').text();

    //值
    var q = $('a');
    var arr = []
    for (let index = 0; index < q.length; index++) {
        const element = q[index];
        var cur_href = element.attribs.href
        if (cur_href !== undefined && cur_href.indexOf("tk") !== -1) {
            var tk_index = cur_href.indexOf("tk")
            var ref = cur_href.slice(tk_index,)
            if (ref != dmc) {
                if (arr.indexOf(ref) == -1) {
                    arr.push(ref)
                }
            }
        }
    }
    ref_map.set(dmc,arr)
}



let txtString = ""
let ref_map = new Map()

for (let index = 0; index < fileArr.length; index++) {
    read(fileArr[index], ref_map)
}
// 往writeme.txt文件 写入一些内容
for (let [key, value] of ref_map) {
    txtString += "dmc: " + key + " ref: "
    for (let index = 0; index < value.length; index++) {
        txtString += value[index] + " "
    }
    txtString += " \n"
}

fs.writeFile(filename, txtString, function (err) {
    // 判断 如果有错 抛出错误 否则 打印写入成功
    if (err) {
        throw err;
    } 
    console.log('写入文件成功!')
})


// const workbook = new Excel.Workbook()
// // workbook.creator = 'test'
// // workbook.lastModifiedBy = 'test'
// // workbook.created = new Date()
// // workbook.modified = new Date()
// const sheet = workbook.addWorksheet('My Sheet');

// sheet.columns = [
//   {header: 'dmc', key: 'dmc', width: 15},
//   {header: 'ref', key: 'ref', width: 15},
// ]
// const data = [{
//   create_time: '2018-10-01',
//   id: '787818992109210'
// }]
// sheet.addRows(data)


// return await workbook.xlsx.writeFile(filename).then( async () => {
//     this.ctx.attachment(`test.xlsx`)
//     this.ctx.type = '.xlsx'
//     this.ctx.body = fs.readFileSync(filePath)
//   }, function (err) {
//     console.log(err)
//   })
// // await workbook.xlsx.writeFile(filename);