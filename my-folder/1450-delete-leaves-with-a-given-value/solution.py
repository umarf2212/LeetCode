# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def deleteLeaf(root, target, isLeafRemoved):
            if not root: return

            if not root.left and not root.right:
                if root.val == target:
                    isLeafRemoved[0] = True
                    return
            
            root.left = deleteLeaf(root.left, target, isLeafRemoved)
            root.right = deleteLeaf(root.right, target, isLeafRemoved)

            return root
        
        while True:
            isLeafRemoved = [False]
            root = deleteLeaf(root, target, isLeafRemoved)
            if not isLeafRemoved[0]:
                break
        
        return root
