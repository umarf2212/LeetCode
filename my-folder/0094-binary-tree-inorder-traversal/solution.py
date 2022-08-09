# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # Morris Inorder Traversal
        ar = []
        while root:
            if not root.left:
                ar.append(root.val)
                root = root.right
            else:
                temp = root.left
                while temp.right and temp.right != root:
                    temp = temp.right
                
                if temp.right == root:
                    ar.append(root.val)
                    root = root.right
                else:
                    temp.right = root
                    root = root.left
        
        return ar
