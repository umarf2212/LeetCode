# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findDepth(self, root):
        if not root: return 0
        return 1 + max(self.findDepth(root.left), self.findDepth(root.right))
        
    
    def dfs(self, root, level, depth, summ):
        if not root: return
            
        if not root.left and not root.right and level == depth:
                summ[0] += root.val
            
        self.dfs(root.left, level+1, depth, summ)
        self.dfs(root.right, level+1, depth, summ)
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        summ = [0]
        depth = self.findDepth(root) - 1
        self.dfs(root, 0, depth, summ)
        
        return summ[0]
