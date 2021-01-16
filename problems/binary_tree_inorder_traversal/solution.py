# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inorder(self, root, ar):
        if root:
            self.inorder(root.left, ar)
            ar.append(root.val)
            self.inorder(root.right, ar)

    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ar = []
        self.inorder(root, ar)
        return ar