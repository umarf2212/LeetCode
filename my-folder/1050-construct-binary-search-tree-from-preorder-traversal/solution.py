# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        root = TreeNode(preorder[0])
        stack = [root]
        i = 1
        while i < len(preorder):
            
            cur = None
            while stack and stack[-1].val < preorder[i]:
                cur = stack.pop()
            
            node = TreeNode(preorder[i])

            if cur:
                cur.right = node
            else:
                stack[-1].left = node
            
            stack.append(node)
            i += 1

        return root
