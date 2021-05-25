# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, arr, targetSum, res):
        if not root: return
        
        arr.append(root.val)
        targetSum -= root.val
                
        if targetSum == 0 and (not root.left and not root.right):
            res.append(list(arr))
        else:
            self.traverse(root.left, arr, targetSum, res)
            self.traverse(root.right, arr, targetSum, res)
        
        arr.pop()
        
    
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        self.traverse(root, [], targetSum, res)

        return res