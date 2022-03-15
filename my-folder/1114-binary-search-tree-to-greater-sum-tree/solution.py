# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def traverse(root,ar):
            if not root: return
            
            traverse(root.left,ar)
            ar.append(root.val)
            traverse(root.right,ar)
        
        ar = []
        traverse(root, ar)
        
        for i in range(len(ar)-2, -1,-1):
            ar[i] = (ar[i+1]+ar[i])

        
        def fillTree(root,i):
            if not root: return
            
            fillTree(root.left,i)
            
            root.val = ar[i[0]]
            i[0]+=1
            
            fillTree(root.right,i)
        
        i=[0]
        fillTree(root,i)
        
        return root
