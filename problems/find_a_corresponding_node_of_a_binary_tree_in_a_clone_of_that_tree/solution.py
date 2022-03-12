# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        # 1. Store pre-order traversal in an array (node)
        # 2. Serialize the Path to the target node
        
        def traverse(root, ar):
            if not root: return
            
            ar.append(root)
            traverse(root.left, ar)
            traverse(root.right, ar)
        
        originalAr = []
        traverse(original, originalAr)
        
        clonedAr = []
        traverse(cloned, clonedAr)
        
        for i in range(len(originalAr)):
            if originalAr[i] == target:
                return clonedAr[i]

        