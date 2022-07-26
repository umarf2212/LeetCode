# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkBST(root, Min, Max):
            if not root: return True
            
            if root.val >= Max or root.val <= Min:
                return False
            
            left = checkBST(root.left, Min, root.val)
            right = checkBST(root.right, root.val, Max)
            
            return left and right
        
        return checkBST(root, float('-inf'), float('inf'))
            
