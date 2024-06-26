# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, root):
        if not root: return False
        
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        
        if not left:
            root.left = None
        
        if not right:
            root.right = None
        
        return left or right or root.val == 1
    
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        res = self.traverse(root)
        if not res: return None
        
        return root
