# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, root, ar):
        if not root: return
        
        self.traverse(root.left, ar)
        ar.append(root.val)
        self.traverse(root.right, ar)

            
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        ar = []
        self.traverse(root, ar)
        
        return ar[k-1]
