/**
 * @param {Array} arr
 * @return {Matrix}
 */
var jsonToMatrix = function(arr) {
    // arr = array of objects or arrays

    const fillObj = (obj, key, resObj) => {
        if (obj === null) return
        Object.keys(obj).sort().map(item => {
            newKey = key + item + '.'
            if (typeof obj[item] === 'object' && obj[item] !== null) {
                fillObj(obj[item], newKey, resObj)
            } else {
                newKey = newKey.slice(0, newKey.length-1)
                resObj[newKey] = obj[item]
                keys.add(newKey)
            }
        })
    }

    let objAr = []
    let keys = new Set()
    arr.forEach(item => {
        let tempObj = {}
        fillObj(item, '', tempObj)
        objAr.push(tempObj)
    })

    let cols = [...keys].sort()

    // console.log(objAr)
    // console.log(cols)

    let resAr = [cols]
    for (let row of objAr) {
        let tempAr = Array(cols.length).fill("")
        Object.keys(row).forEach(item => {
            tempAr[cols.indexOf(item)] = row[item]
        })
        resAr.push(tempAr)
    }

    return resAr

    // console.log(resAr)

    // 1 3 x
    // 2 x x
    // x x 4


    // Object.keys(resObj)

};
