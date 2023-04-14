/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    if (n === 0) return arr

    function flatten(arr, flat_arr, depth, n) {
        arr.forEach(item => {
            if (typeof item === 'object' && depth < n) {
                flatten(item, flat_arr, depth+1, n)
            }
            else {
                flat_arr.push(item)
            }
        })
    }

    let flat_arr = []
    flatten(arr, flat_arr, 0, n)
    return flat_arr
};
