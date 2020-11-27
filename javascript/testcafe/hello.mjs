function sliceArray(anim, beginSlice, endSlice) {
    // 请在本行以下添加你的代码
    let new = [];
    for(let i = beiginSlice; i < endSlice; i++){
      new.push(anim[i]);
    }
    return new;
    // 请在本行以上添加你的代码
  }
  var inputAnim = ["Cat", "Dog", "Tiger", "Zebra", "Ant"];
  sliceArray(inputAnim, 1, 3);