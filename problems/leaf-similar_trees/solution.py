# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, root, ar):
        if not root: return
        
        if not root.left and not root.right:
            ar.append(root.val)
            
        self.dfs(root.left, ar)
        self.dfs(root.right, ar)

    
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        ar1 = []
        ar2 = []
        
        self.dfs(root1, ar1)
        self.dfs(root2, ar2)
        
        if len(ar1) != len(ar2): return False
        
        for i in range(len(ar1)):
            if ar1[i] != ar2[i]:
                return False
            
        return True