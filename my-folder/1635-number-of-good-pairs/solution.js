/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function(nums) {
    
    let f = x => x<=1 ? 1 : x*f(x-1)
    let comb = (n, r) => f(n) / (f(r) * f(n-r))
    
    let map = new Map()
    
    for (let num of nums) {
        if (!map.has(num)) {
            map.set(num, 1)
        }
        else {
            map.set(num, map.get(num)+1)
        }
    }
    
    let totalCount = 0
    for (entry of map.entries()) {
        if (entry[1] > 1) {
            totalCount += comb(entry[1], 2)
        }
    }
    
    return totalCount
    
};
