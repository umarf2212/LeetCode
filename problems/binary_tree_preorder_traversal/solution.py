# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def preorder(self, root, ar):
        if root:
            ar.append(root.val)
            self.preorder(root.left, ar)
            self.preorder(root.right, ar)
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ar = []
        self.preorder(root, ar)
        return ar