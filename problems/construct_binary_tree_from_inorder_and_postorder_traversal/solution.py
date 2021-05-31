# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def build(self, postorder, inorder, start, end):
        if not postorder: return
        if start > end: return None
        
        currValue = postorder.pop()
        
        root = TreeNode(currValue)
        
        i = inorder[currValue]
        root.right = self.build(postorder, inorder, start, i-1)
        root.left = self.build(postorder, inorder, i+1, end)
        
        return root
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        d = {inorder[len(inorder)-1-i]:i for i in range(len(inorder))}
        # d = {inorder[i]:i for i in range(len(inorder))}

        return self.build(postorder, d, 0, len(postorder))