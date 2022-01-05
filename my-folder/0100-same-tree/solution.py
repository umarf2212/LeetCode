# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traverse(root1, root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            
            if root1.left and not root2.left or \
            not root1.left and root2.left or \
            root1.right and not root2.right or \
            not root1.right and root2.right:
                return False
            
            if (root1.left and root2.left and root1.left.val != root2.left.val) or \
            (root1.right and root2.right and root1.right.val != root2.right.val):
                return False
            
            return traverse(root1.left, root2.left) and \
        traverse(root1.right, root2.right)
        
        if p and q and p.val != q.val: return False
        return traverse(p, q)
