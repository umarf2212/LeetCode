# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, root, tiltSum):
        if not root: return 0
        
        left = self.traverse(root.left, tiltSum)
        right = self.traverse(root.right, tiltSum)
        
        tiltSum[0] += abs(left-right)
        
        return root.val + left + right
        
    
    def findTilt(self, root: TreeNode) -> int:
        tiltSum = [0]
        
        self.traverse(root, tiltSum)
        return tiltSum[0]
