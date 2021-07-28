# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def makeList(self, root, ar):
        if not root: return
        
        ar.append(root.val)
        self.makeList(root.left, ar)
        self.makeList(root.right, ar)
        
    
        def buildLinkedList(self, root, ar):
            if not ar: return None
            
            new = TreeNode(root.val)
            new.right = self.buildLinkedList(root.right, ar[1:])
            
            return new
    
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        ar = []
        self.makeList(root, ar)
        temp = root
        if len(ar) > 0: temp.val = ar[0]
        for i in range(1, len(ar)):
            if temp.right:
                temp.right.val = ar[i]
            else:
                temp.right = TreeNode(ar[i])
            
            temp.left = None
            temp = temp.right