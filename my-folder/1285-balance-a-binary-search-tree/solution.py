# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def inorder(node, treeArray):
            if not node:
                return
            
            inorder(node.left, treeArray)
            treeArray.append(node.val)
            inorder(node.right, treeArray)
        
        treeArray = []
        inorder(root, treeArray)

        def recreateBST(left, right, currArray):
            if left > right:
                return None
            
            if left == right:
                return TreeNode(currArray[left])
            
            mid = (left + right)//2

            curr = TreeNode(currArray[mid])

            curr.left = recreateBST(left, mid-1, currArray)
            curr.right = recreateBST(mid+1, right, currArray)

            return curr
        
        return recreateBST(0, len(treeArray)-1, treeArray)

