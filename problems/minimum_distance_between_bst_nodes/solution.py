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

        
    def minDiffInBST(self, root: TreeNode) -> int:
        ar = []
        self.traverse(root, ar)
        
        diff = float('inf')
        print(ar)
        for i in range(1,len(ar)):
            diff = min(diff, ar[i]-ar[i-1])
        
        
        return diff