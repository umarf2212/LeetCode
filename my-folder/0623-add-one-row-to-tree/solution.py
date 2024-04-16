# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        
        def dfs(root, curDepth):
            if not root: return root

            if curDepth == depth-1:
                left = root.left
                right = root.right

                root.left = TreeNode(val)
                root.right = TreeNode(val)

                root.left.left = left
                root.right.right = right
                return

            dfs(root.left, curDepth+1)
            dfs(root.right, curDepth+1)
        
        dfs(root, 1)
        return root




