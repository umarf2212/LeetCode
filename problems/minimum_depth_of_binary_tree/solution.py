# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, root):
        if not root: return 0
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        
        if left==0 or right==0:
            return 1 + max(left, right)
        else:
            return 1 + min(left, right)
            
        # if left > 0 and right > 0:
        #     return 1 + min(left, right)
        # else:
        #     return 1 + max(left, right)
        
    
    def minDepth(self, root: TreeNode) -> int:
        
        return self.traverse(root)