# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def traverse(root):
            if not root: return

            if root.val == 1 or root.val == 0: 
                return root.val

            left = traverse(root.left)
            right = traverse(root.right)

            return left or right if root.val == 2 else left and right
        
        return True if traverse(root) == 1 else False
