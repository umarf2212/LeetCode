# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def postorder(self, root, ar):
        if root:
            self.postorder(root.left, ar)
            self.postorder(root.right, ar)
            ar.append(root.val)
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ar = []
        self.postorder(root, ar)
        return ar