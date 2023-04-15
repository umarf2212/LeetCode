/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    /**
        THIS IS A BRUTEFORCE APPROACH
     */
    if (rowsCount * colsCount !== this.length) return []
    let ar = this
    let cur = []
    let res = []
    col = 0
    let i = 0
    while (i < ar.length) {
        cur.push(ar[i])

        // cur col done, make new one, add to result
        if ((i+1) % rowsCount == 0) {
            if (col%2 == 0) {
                res.push(cur)
            } else {
                res.push(cur.reverse())
            }
            cur = []
            col += 1
        }
        i+=1
    }
    
    // recreate the matrix
    ans = []
    row = 0
    while (row < rowsCount) {
        cur = []
        for (let i=0; i<res.length; i++) {
            cur.push(res[i][row])
        }
        ans.push(cur)
        row += 1
    }
    return ans
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */