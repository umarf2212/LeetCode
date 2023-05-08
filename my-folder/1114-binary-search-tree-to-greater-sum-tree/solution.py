# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    curSum = 0
    def traverse(self, root):
        if not root: return 0

        self.traverse(root.right)

        self.curSum += root.val
        root.val = self.curSum 

        self.traverse(root.left)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        return root


