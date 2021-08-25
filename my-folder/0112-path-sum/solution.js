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
 * @param {number} targetSum
 * @return {boolean}
 */

var traverse = function(root, targetSum) {
    if (root === null) return false
    
    if (root.left === null && root.right === null && targetSum-root.val===0) {
        return true
    }
    
    var left = traverse(root.left, targetSum-root.val)
    var right = traverse(root.right, targetSum-root.val)
    return left || right
    
}

var hasPathSum = function(root, targetSum) {
    if (root === null) return false
    return traverse(root, targetSum)
};
