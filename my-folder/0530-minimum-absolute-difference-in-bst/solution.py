# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorder(self, root, ar):
        if not root: return
        
        self.inorder(root.left, ar)
        ar.append(root.val)
        self.inorder(root.right, ar)

    
    def getMinimumDifference(self, root: TreeNode) -> int:
        ar = []
        
        self.inorder(root, ar)
        
        minDiff = float('inf')
        for i in range(1, len(ar)):
            d = abs(ar[i] - ar[i-1])
            if d < minDiff:
                minDiff = d
        
        return minDiff
