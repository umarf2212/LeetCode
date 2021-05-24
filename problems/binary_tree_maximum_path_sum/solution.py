# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, root, maxSoFar):
        if not root: return 0
        
        left = self.traverse(root.left, maxSoFar)
        right = self.traverse(root.right, maxSoFar)
        
        curr_max = max(root.val, root.val+left, root.val+right)
        
        maxSoFar[0] = max(maxSoFar[0], curr_max, root.val+left+right)
        
        return curr_max
    
    def maxPathSum(self, root: TreeNode) -> int:
        
        maxSoFar = [float('-inf')]
        
        self.traverse(root, maxSoFar)
        
        return maxSoFar[0]
        