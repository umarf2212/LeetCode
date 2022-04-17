# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def traverse(root):
            if not root: return None
            
            if not root.left and not root.right and root.val == target:
                return None
        
            root.left = traverse(root.left)
            root.right = traverse(root.right)
                
            if not root.left and not root.right and root.val == target:
                return None
            else:
                return root
    
        root = traverse(root)
        return root
            
