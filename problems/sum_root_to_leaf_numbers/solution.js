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
 * @return {number}
 */
var traverse = function(root, currNum, numbers) {
    if (root === null) return
    
    currNum.push(root.val)
    
    if (root.left === null && root.right === null) {
        
        // currNum = [1,2,3,4]
        // Number(currNum.join('')) -> 1234
        numbers['num'] += Number(currNum.join(''))
    }
    
    traverse(root.left, currNum, numbers)
    traverse(root.right, currNum, numbers)
    
    currNum.pop()

    
}

var sumNumbers = function(root) {
    var numbers = {num:0}
    var currNum = []
    traverse(root, currNum, numbers)
    return numbers['num']
};

