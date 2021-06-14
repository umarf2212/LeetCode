# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def depth(self, root):
        if not root: return 0
        return 1 + max(self.depth(root.left), self.depth(root.right))
    
    def dfs(self, root, level, depth, res):
        if not root: return
        
        if level == depth-1:
            if root.left and not root.left.left and not root.left.right:
                res.append(root.left.val)
            elif root.right and not root.right.left and not root.right.right:
                res.append(root.right.val)
        
        self.dfs(root.left, level+1, depth, res)
        self.dfs(root.right, level+1, depth, res)

        
    
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root.left and not root.right: return root.val
        
        res = []
        depth = self.depth(root)
        self.dfs(root, 1, depth, res)
        return res[0]