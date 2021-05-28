# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def invert(self, root):
        if not root: return
        
        left = self.invert(root.left)
        right = self.invert(root.right)
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        return root
        
        
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        return self.invert(root)