function takeLongTime(n) {
    return new Promise( resolve => {
        setTimeout( () => resolve(n + 200), n)
    })
}

function step1(n) {
    console.log(`step1 with ${n}`);
    return takeLongTime(n)
}

function step2(n) {
    console.log(`step2 with ${n}`);
    return takeLongTime(n)
}

function step3(n) {
    console.log(`step3 with ${n}`);
    return takeLongTime(n)
}


// console.timeEnd() 方法是作为计算器的结束方法。
// 该方法一般用于测试程序执行的时长。
// console.time() 方法为计算器的起始方法。
// console.timeEnd() 方法为计算器的结束方法，并将执行时长显示在控制台。

function doIt() {
    console.time("doIt");
    const time1 = 300

    step1(time1)
        .then(time2 => step2(time2))
        .then(time3 => step3(time3))
        .then(result => {
            console.log(`result is ${result}`);
            console.timeEnd("doIt");
        })
}

doIt()