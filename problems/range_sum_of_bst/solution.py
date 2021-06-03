# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, root, low, high, totalSum):
        if not root: return
        

        self.traverse(root.left, low, high, totalSum)

        if root.val in range(low, high+1):
            totalSum.append(root.val)
        
        self.traverse(root.right, low, high, totalSum)
            
    
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        totalSum = []
        self.traverse(root, low, high, totalSum)
        return sum(totalSum)