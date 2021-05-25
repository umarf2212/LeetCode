# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, root, targetSum):
        if not root: return
        
        #leaf
        if (not root.left and not root.right) and targetSum-root.val == 0:
            return True
    
        left = self.traverse(root.left, targetSum-root.val)
        right = self.traverse(root.right, targetSum-root.val)
        
        return left or right
    
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root: return False
        
        return self.traverse(root, targetSum)
