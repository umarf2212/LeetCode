# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def validate(self, root, mmin, mmax):
        if not root: return True
        
        if root.val >= mmax or root.val <= mmin:
            return False
        
        return self.validate(root.left, mmin, root.val) and self.validate(root.right, root.val, mmax)

    
    def isValidBST(self, root: TreeNode) -> bool:
        if not root.left and not root.right: return True
        
        return self.validate(root.left, float('-inf'), root.val) and self.validate(root.right, root.val, float('inf'))
