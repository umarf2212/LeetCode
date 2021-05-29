# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findSum(self, root):
        if not root: return 0
        
        if root:
            summ = self.findSum(root.left) + self.findSum(root.right)

        if root.left and not root.left.left and not root.left.right:
            return root.left.val + summ
        else:
            return summ
    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        summ = [0]
        return self.findSum(root)
        return summ[0]
