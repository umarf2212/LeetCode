# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def traverse(node, p, q, lca):
            if not node: 
                return False
            
            left = traverse(node.left, p, q, lca)
            right = traverse(node.right, p, q, lca)

            if left and right:
                lca[0] = node
            
            if node.val == p.val or node.val == q.val:
                if left or right:
                    lca[0] = node
                else:
                    return True

            return left or right
        
        lca = [None]
        traverse(root, p, q, lca)
        return lca[0]
