# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, root, ar):
        if not root: return
        
        self.traverse(root.left, ar)
        ar.append(root.val)
        self.traverse(root.right, ar)
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        res = []
        
        self.traverse(root1, res)
        self.traverse(root2, res)
        
        res.sort()
        
        return res
