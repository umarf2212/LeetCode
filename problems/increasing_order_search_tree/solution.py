# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorder(self, root, ar):
        if not root: return
        self.inorder(root.left, ar)
        ar.append(root.val)
        self.inorder(root.right, ar)
    
    def tree(self, i, ar):
        if i == len(ar): return None
        
        root = TreeNode(ar[i])
        root.right = self.tree(i+1, ar)
        return root

    def increasingBST(self, root: TreeNode) -> TreeNode:
        ar = []
        self.inorder(root, ar)
        return self.tree(0, ar)