# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        # preIndex[0] -> preorder[preIndex[0]]
    
    def build(self, preorder, inorder, start, end):
        if not preorder: return
        if start > end: return None
        
        currValue = preorder.pop()
        
        root = TreeNode(currValue)
        
        i = inorder[currValue]
        root.left = self.build(preorder, inorder, start, i-1)
        root.right = self.build(preorder, inorder, i+1, end)
        
        return root

    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        d = {inorder[i]:i for i in range(len(inorder))}
        preorder = [preorder[len(preorder)-i-1] for i in range(len(preorder))]

        return self.build(preorder, d, 0, len(preorder))