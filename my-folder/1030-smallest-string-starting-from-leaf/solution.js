/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {string}
 */

var smallestFromLeaf = function(root) {
    
    var traverse = function(root) {
        if (root === null) return

        currStr.push(alpha[root.val])
        
        if (root.left===null && root.right===null) {
            let str = ''
            for (let i=currStr.length-1; i>=0; i--) {
                str += currStr[i]
            }
            res.push(str)
        }

        traverse(root.left)
        traverse(root.right)
        
        currStr.pop()
    
    }
    
    var res = []
    var currStr = []
    var alpha = 'abcdefghijklmnopqrstuvwxyz'
    traverse(root, currStr)
    
    let smallest = res[0]
    for (let str of res) {
        if (str < smallest) {
            smallest = str
        }
    }
    console.log(res)
    return smallest
};
