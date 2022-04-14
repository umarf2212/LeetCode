# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        
        def traverse(root, ans):
            if not root: return None
            
            if root.val == val:
                ans[0] = root
            
            if root.val > val:
                traverse(root.left, ans)
            else:
                traverse(root.right, ans)
        
        ans = [None]
        traverse(root, ans)
        
        return ans[0]