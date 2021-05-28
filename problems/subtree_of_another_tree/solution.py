# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def match(self, root, sub):
        
        if not root and not sub:
            return True
        elif not root or not sub:
            return False
        elif root.val != sub.val:
            return False
        else:
            return self.match(root.left, sub.left) and self.match(root.right, sub.right)
        
        
    def matchNodes(self, root, sub):
        if not root: return
        
        foundSubtree = False
        if root.val == sub.val:
            foundSubtree = self.match(root, sub)
        
        return self.matchNodes(root.left, sub) or self.matchNodes(root.right, sub) or foundSubtree

    
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        return self.matchNodes(root, subRoot)