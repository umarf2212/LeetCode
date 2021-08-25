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
 * @return {number[]}
 */

var traverse = function(root, ar) {
    if (root === null) return null

    traverse(root.left, ar)
    ar.push(root.val)
    traverse(root.right, ar)
    
}

var inorderTraversal = function(root) {
    let ar = []
    traverse(root, ar)
    return ar
};
