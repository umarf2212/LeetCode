# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return False
        
        # 1. Do postorder traversal
        # 2. Return the result of left subtree and right subtree
        #    and evaluate current cell, and return to its parent

        def traverse(root):
            if not root: return
            
            # if leaf node
            if not root.left and not root.right:
                return True if root.val == 1 else False
            
            left = traverse(root.left)
            right = traverse(root.right)

            if root.val == 2:
                curRes = left or right
            else:
                curRes = left and right
            
            return curRes
        
        return traverse(root)
            

