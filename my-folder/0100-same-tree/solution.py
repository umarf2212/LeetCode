# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, t1, t2):
        if not t1 and not t2:
            return True
        elif not t1 or not t2:
            return False
        elif t1.val != t2.val:
            return False
        else:
            return self.traverse(t1.left, t2.left) and self.traverse(t1.right, t2.right)
    
    def preorder(self, root, res):
        if not root: 
            res.append(root)
            return
        
        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        
        ar1 = []
        ar2 = []
        
        self.preorder(p, ar1)
        self.preorder(q, ar2)
        
        return ar1==ar2
        
        # return self.traverse(p, q)
