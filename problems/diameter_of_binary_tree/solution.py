# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, root, max_so_far):
        if not root: return 0
        
        left = self.traverse(root.left, max_so_far)
        right = self.traverse(root.right, max_so_far)
        
        curr_max = max(1 + left, 1 + right)
        max_so_far[0] = max(curr_max, 1+left+right, max_so_far[0])
        # print(max_so_far[0])
        
        return curr_max
        
        
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ar = [0]
        
        self.traverse(root, ar)
        return ar[0] -1