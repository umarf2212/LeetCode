# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # This is a simple Bruteforce approach to check of Two Trees match

        def checkMatch(p, q):
            if not p and not q: return True
            if not p or not q: return False
            if p.val != q.val: return False
            return checkMatch(p.left, q.left) and checkMatch(p.right, q.right)
        
        def traverse(root1, root2):
            if not root1 and not root2: return
            if not root1 or not root2: return

            if checkMatch(root1, root2):
                return True
            
            return traverse(root1.left, root2) or traverse(root1.right, root2)

        return traverse(root, subRoot)
