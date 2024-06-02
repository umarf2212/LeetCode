# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        # 1. Parent will remove the node of the children if either of them is in to_delete
        
        def dfs(root, to_delete, result):
            if not root: 
                return
            
            if root.val in to_delete:
                if root.left:
                    result.add(root.left)
                if root.right:
                    result.add(root.right)
            
            dfs(root.left, to_delete, result)
            dfs(root.right, to_delete, result)
            
            if root.left and root.left.val in to_delete:
                root.left = None
            
            if root.right and root.right.val in to_delete:
                root.right = None
            
        result = set()
        result.add(root)
        to_delete = set(to_delete)
        dfs(root, to_delete, result)

        finalResult = [node for node in result if node.val not in to_delete]
        return finalResult
            

