# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, root):
        if not root: return 0
        
        Sum = 0
        if root.val % 2 == 0:
            if root.left:
                if root.left.left:
                    Sum += root.left.left.val
                
                if root.left.right:
                    Sum += root.left.right.val
            
            if root.right:
                if root.right.left:
                    Sum += root.right.left.val
                
                if root.right.right:
                    Sum += root.right.right.val
            
        if root.left:
            Sum += self.traverse(root.left)
        
        if root.right:
            Sum += self.traverse(root.right)
        
        return Sum
            
    
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        return self.traverse(root)
