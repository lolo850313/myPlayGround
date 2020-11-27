fs.writeFile(filename, txtString, function (err) {
            // 判断 如果有错 抛出错误 否则 打印写入成功
            if (err) {
                throw err;
            } 
            console.log('写入文件成功!')
        })
        