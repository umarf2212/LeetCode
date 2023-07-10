# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def traverse(root):
            if not root: 
                return 0

            left = traverse(root.left)
            right = traverse(root.right)

            if left > 0 and right > 0:
                return 1 + min(left, right)
                
            return 1 + max(left, right)
        
            
        return traverse(root)
