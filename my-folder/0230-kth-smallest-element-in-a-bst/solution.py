# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def traverse(root, k, res):
            if not root: return

            traverse(root.left, k, res)

            k[0] -= 1
            if not k[0]:
                res[0] = root

            traverse(root.right, k, res)
        
        res = [root]
        k = [k]
        traverse(root, k, res)
        return res[0].val
