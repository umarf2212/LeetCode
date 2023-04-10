# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # This solution is strongly inspired by Morris inorder traversal
        # This is a memory-time tradeoff.
        # In-place means constant memory usage which is a big deal and 
        # is compensated with by extra time.

        def moveNodes(root):
            if not root: return

            if (not root.left and not root.right) or (not root.left and root.right):
                return root
            
            if not root.right and root.left:
                root.right = root.left
                root.left = None
            
            if root.left and root.right:
                temp = root.left
                while temp.right:
                    temp = temp.right
                
                temp.right = root.right
                root.right = root.left
                root.left = None
            
            return root
        
        def flatten(root):
            if not root: return
            if not root.left and not root.right:
                return
            
            flatten(root.right)
            flatten(root.left)
            return moveNodes(root)
        
        return flatten(root)

