# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, root):
        if not root: return None
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        
        st = ''
        if left and not right:
            st += '('+str(left)+')'
        elif not left and right:
            st += '()('+str(right)+')'
        elif left and right:
            st += '('+str(left)+')' + '('+str(right)+')'
            
        return str(root.val) + st
    
    def tree2str(self, root: TreeNode) -> str:
        return self.traverse(root)