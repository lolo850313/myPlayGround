var fs = require('fs');
var cheerio = require('cheerio');

var myHtml = fs.readFileSync("D:\\工作文档\\pdf结构化\\test.html");
var $ = cheerio.load(myHtml);
console.log($)
var t = $('html').find('hr');
var t2 = t.nextAll();

t2.each(function(i, elem) {
    getContent($(this));
    console.log($(this).text());
});