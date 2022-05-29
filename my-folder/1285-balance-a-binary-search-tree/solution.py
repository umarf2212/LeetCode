# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:        
        def inorder(root, arr):
            if not root: return
            
            inorder(root.left, arr)
            arr.append(root.val)
            inorder(root.right, arr)
        
        def build(arr, i, j):
            if i>j: return None
            
            mid = (j+i)//2
            newNode = TreeNode(arr[mid])
            newNode.left = build(arr, i, mid-1)
            newNode.right = build(arr, mid+1, j)
            
            return newNode
        
        
        arr = []
        inorder(root, arr)
        
        return build(arr, 0, len(arr)-1)       
            
