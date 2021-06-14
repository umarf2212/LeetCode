# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, ar):
        if not ar: return None
        
        mx = 0
        for i in range(len(ar)):
            if ar[i] > ar[mx]:
                mx = i
        
        root = TreeNode(ar[mx])
        root.left = self.traverse(ar[:mx])
        root.right = self.traverse(ar[mx+1:])
        
        return root
        
    
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.traverse(nums)