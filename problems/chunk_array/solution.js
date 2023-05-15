/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    // [0 1 2 3] [4 5 6 7] 8 9 
    let res = []
    let i = 0
    let temp = []
    while (i < arr.length) {
        temp.push(arr[i])
        if ((i+1) % size === 0 || i === arr.length-1) {
            res.push(temp)
            temp = []
        }
        i++
    }
    return res
};