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
 * @return {TreeNode}
 */
var pruneTree = function(root) {
    
    var traverse = function(root) {
        if (root===null) return false
        
        let left = traverse(root.left)
        let right = traverse(root.right)
        
        if (!left) {
            root.left = null
        }
        if (!right) {
            root.right = null
        }

        return left || right || root.val === 1
        
    }
    
    let res = traverse(root)
    if (!res) return null
    
    return root
    
};