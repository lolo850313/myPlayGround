var http = require('http'),fs = require('fs');
path = "D:\\迅雷下载\\"
http.get(path,function(req,res){  //path为网络图片地址
  var imgData = '';
  req.setEncoding('binary');
  req.on('data',function(chunk){
    imgData += chunk
  })
  req.on('end',function(){
    fs.writeFile(path,imgData,'binary',function(err){  //path为本地路径例如public/logo.png
      if(err){console.log('保存出错！')}else{
        console.log('保存成功!')
      }
    })
  })
})