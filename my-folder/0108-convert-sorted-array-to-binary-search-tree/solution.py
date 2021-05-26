# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def makeBST(self, ar, left, right):
        if left > right: return None
        
        mid = left + (right-left)//2
        newNode = TreeNode(ar[mid])
        
        newNode.left = self.makeBST(ar, left, mid-1)
        newNode.right = self.makeBST(ar, mid+1, right)
        
        return newNode
        
    
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        return self.makeBST(nums, 0, len(nums)-1)
