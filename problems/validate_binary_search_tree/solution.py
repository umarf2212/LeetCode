# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(root, Min, Max):
            if not root: return True

            if root.val >= Max or root.val <= Min:
                return False
            
            left = validate(root.left, Min, root.val)
            right = validate(root.right, root.val, Max)
        
            return left and right

        return validate(root, float('-inf'), float('inf'))