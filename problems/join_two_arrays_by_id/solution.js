/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    let map = new Map()
    for (let item of arr1) {
        map.set(item.id, item)
    }

    for (let item of arr2) {
        if (map.has(item.id)) {
            map.set(item.id, {...map.get(item.id), ...item})
        } else {
            map.set(item.id, item)
        }
    }

    let res = []
    for (let [_, obj] of map) {
        res.push(obj)
    }

    res.sort((a, b) => a['id'] - b['id'])

    return res
};