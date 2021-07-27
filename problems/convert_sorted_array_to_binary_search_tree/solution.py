# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def buildTree(self, nums):
        if not nums: return None
        
        mid = (len(nums)-1) // 2
        
        root = TreeNode(nums[mid])
        
        root.left = self.buildTree(nums[:mid])
        root.right = self.buildTree(nums[mid+1:])
        
        return root
        
    
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        return self.buildTree(nums)