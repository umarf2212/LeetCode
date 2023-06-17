# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:

        def dfs(root, n, depth):
            if not root: 
                return
            
            if n == depth:
                return root
            
            left = dfs(root.left, n+1, depth)
            right = dfs(root.right, n+1, depth)

            if left and right:
                return root
            
            if not left and not right:
                return
            
            return left if left else right
        
        def findDepth(root):
            if not root: return 0
            return 1 + max(findDepth(root.left), findDepth(root.right))
        
        depth = findDepth(root)
        
        return dfs(root, 1, depth)
