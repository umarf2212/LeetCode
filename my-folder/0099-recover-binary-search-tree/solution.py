# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def traverse(root, ar):
            if not root: return
            
            traverse(root.left, ar)
            ar.append(root)
            traverse(root.right, ar)
        
        ar = []
        traverse(root, ar)
        ar_sorted = sorted(ar, key=lambda x:x.val)
    
        anomalies = []
        for i in range(len(ar)):
            if ar[i].val != ar_sorted[i].val:
                anomalies.append(ar[i])
        anomalies[0].val, anomalies[1].val = anomalies[1].val, anomalies[0].val
                
        
        
