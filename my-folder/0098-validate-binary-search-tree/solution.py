# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(root, curMax, curMin):
            if not root: return True

            if root.val >= curMax:
                return False
            
            if root.val <= curMin:
                return False
            
            return validate(root.left, root.val, curMin) and validate(root.right, curMax, root.val)
    
        return validate(root, float('inf'), float('-inf'))
