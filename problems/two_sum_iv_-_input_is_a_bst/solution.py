# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def find(self, root, k, d):
        if not root: return False
        
        diff = k - root.val
        
        if diff in d:
            return True
        else:
            d.add(root.val)
        
        return self.find(root.right, k, d) or self.find(root.left, k, d)
        
    
    def findTarget(self, root: TreeNode, k: int) -> bool:
        d = set()
        
        return self.find(root, k, d)