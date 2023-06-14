# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def traverse(root, ar):
            if not root: return

            traverse(root.left, ar)
            ar.append(root.val)
            traverse(root.right, ar)
        
        ar = []
        traverse(root, ar)

        diff = float('inf')
        for i in range(len(ar)-1):
            diff = min(diff, ar[i+1]-ar[i])

        return diff