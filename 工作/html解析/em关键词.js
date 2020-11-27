const fs = require('fs');
const cheerio = require('cheerio');
const path = require("path")
const filename = 'em关键词.txt'
const words = new Set(["as necessary", "recommend", 'suggest', 'better', 'best', 'if necessary',"As necessary", "Recommend", 'Suggest', 'Better', 'Best', 'If necessary'])

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


add_doc(dir,docArr)

function add_html(docArr) {
    function writeInfo(fileArr) {
        let txtString = ""
        let ref_map = []
    
        let filename = dir + fileArr[0].split("\\")[3] + ".txt"
        console.log(filename)
    
        for (let index = 0; index < fileArr.length; index++) {
            read(fileArr[index], ref_map)
        }
        // 往writeme.txt文件 写入一些内容
        for (let i of ref_map) {
            txtString += '@@@' + i[0] + "@" + i[1] + "@" + i[2] + "@" + i[3]
        }
    
        fs.writeFile(filename, txtString, function (err) {
            // 判断 如果有错 抛出错误 否则 打印写入成功
            if (err) {
                throw err;
            } 
            console.log('写入文件成功!')
        })
        
    }

    for (let index = 0; index < docArr.length; index++) {
        const subArr = docArr[index];
        let fileArr = []
        fs.readdirSync(subArr).forEach(function (file) {
            const pathname = path.join(subArr, file)
            fileArr.push(pathname)
        })
        writeInfo(fileArr)
    }
}

add_html(docArr)

function read(input, ref_map) {
    let myHtml = fs.readFileSync(input);
    let $ = cheerio.load(myHtml);

    let filename = input.split("\\")[3]
    // title
    let title = $('title').text();

    let tmp = input.split("\\")
    let name = tmp[tmp.length - 1]

    let all = $('*')
    for (let index = 0; index < all.length; index++) {
        const child_arr = all[index].children;
        // console.log(child.type)
        for (let index = 0; index < child_arr.length; index++) {
            const element = child_arr[index];
            if (element.type === "text") {
                const element_text = (element.data)
                for (let word of words) {
                    if (element_text.indexOf(word) !== -1) {
                        ref_map.push([filename ,title, word, element_text])
                    }
                    
                }
            }
        }
        
        
    }
}

