function sliceArray(anim, beginSlice, endSlice) {
    // ���ڱ������������Ĵ���
    let new = [];
    for(let i = beiginSlice; i < endSlice; i++){
      new.push(anim[i]);
    }
    return new;
    // ���ڱ������������Ĵ���
  }
  var inputAnim = ["Cat", "Dog", "Tiger", "Zebra", "Ant"];
  sliceArray(inputAnim, 1, 3);