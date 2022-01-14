# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        
        
        def traverse(root, n, k, res):
            if not root: return
            
            traverse(root.left, n, k, res)       
            
            n[0] +=1
            if n[0] == k:
                res[0] = root.val
            
            traverse(root.right, n, k, res)            


        
        n = [0]
        res = [0]
        traverse(root, n, k, res)
        
        return res[0]