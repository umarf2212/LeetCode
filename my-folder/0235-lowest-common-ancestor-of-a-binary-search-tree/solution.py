# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def traverse(root, p, q):
            if not root: return None
            
            if root.val >= p.val and root.val <= q.val:
                return root
            
            elif root.val < p.val and root.val < q.val:
                return traverse(root.right, p, q)
            
            return traverse(root.left, p, q)
                
        return traverse(root, p if p.val<q.val else q, q if q.val>p.val else p)
