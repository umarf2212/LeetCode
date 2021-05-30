# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def find(self, root, val):
        if not root: return
        
        if root.val == val:
            return root
        elif val > root.val:
            return self.find(root.right, val)
        else:
            return self.find(root.left, val)
    
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.find(root, val)
