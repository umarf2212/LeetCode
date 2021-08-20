/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 */
var numJewelsInStones = function(jewels, stones) {
    
    var set = new Set();
    
    for (let i of jewels) set.add(i);
    
    let count = 0
    for (let i of stones) {
        if (set.has(i)) count++;
    }
    
    return count
};
