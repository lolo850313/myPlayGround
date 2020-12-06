// 防抖：n秒内函数只执行一次
function debounce( fn ) {
    let timeout = null
    return function () {
        clearTimeout(timeout)
    }
}