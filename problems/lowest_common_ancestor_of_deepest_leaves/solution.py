# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def findDepth(root):
            if not root: return 0
            return 1 + max(findDepth(root.left), findDepth(root.right))
        
        depth = findDepth(root)

        def traverse(root, n, depth):
            if not root: return

            if n == depth:
                return root
            
            left = traverse(root.left, n+1, depth)
            right = traverse(root.right, n+1, depth)

            if left and right:
                return root
            
            if not left and not right:
                return
            
            return left if left else right
        
        return traverse(root, 1, depth)
