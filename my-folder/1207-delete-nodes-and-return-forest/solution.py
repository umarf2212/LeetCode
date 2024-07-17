# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        
        def deleteNodes(node, to_delete, remaining):
            if not node: 
                return
            
            if node.val in to_delete:
                if node.left:
                    remaining.append(node.left)
                
                if node.right:
                    remaining.append(node.right)
            
            deleteNodes(node.left, to_delete, remaining)
            deleteNodes(node.right, to_delete, remaining)

            if node.left and node.left.val in to_delete:
                node.left = None
            
            if node.right and node.right.val in to_delete:
                node.right = None
            
        
        to_delete = set(to_delete)
        remaining = [root]

        deleteNodes(root, to_delete, remaining)

        result = [node for node in remaining if node.val not in to_delete]
        
        return result



