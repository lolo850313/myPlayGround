// ȫ�ֱ���
var globalTitle = " Winter Is  ?Coming";

// ���ڱ������������Ĵ���
function urlSlug(title) {
  let res = title.toLowerCase()
  let q = res.split(" ")
  return q.join("-")
  
}
// ���ڱ������������Ĵ���

var winterComing = urlSlug(globalTitle); // ӦΪ "winter-is-coming"
console.log(winterComing)