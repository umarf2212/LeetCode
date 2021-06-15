# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, root, low, high):
        if not root: return
        
        if root.val >= low and root.val <= high:
            newRoot = root
            newRoot.left = self.traverse(root.left, low, high)
            newRoot.right = self.traverse(root.right, low, high)
        else:
            if root.val < low:
                newRoot = self.traverse(root.right, low, high)
            elif root.val > high:
                newRoot = self.traverse(root.left, low, high)
            
        return newRoot
        
    
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        return self.traverse(root, low, high)
