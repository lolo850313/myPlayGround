// 全局变量
var globalTitle = " Winter Is  ?Coming";

// 请在本行以下添加你的代码
function urlSlug(title) {
  let res = title.toLowerCase()
  let q = res.split(" ")
  return q.join("-")
  
}
// 请在本行以上添加你的代码

var winterComing = urlSlug(globalTitle); // 应为 "winter-is-coming"
console.log(winterComing)