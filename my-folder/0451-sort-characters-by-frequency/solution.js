/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    
    var map = new Map()
    
    for (let i of s) {
        if (map.has(i)) {
            map.set(i, map.get(i)+1)
        }
        else {
            map.set(i, 1)
        }
    }
    
    let ar = Array.from(map).sort((a,b) => b[1]-a[1])
    
    let res = ''
    for (let i of ar) {
        res += i[0].repeat(i[1])
    }
    
    return res
};
