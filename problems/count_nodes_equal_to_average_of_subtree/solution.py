# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root, res):
            if not root: return [0,0]
            # [number of nodes, running sum]

            left = traverse(root.left, res)
            right = traverse(root.right,res)

            currAvg = [1+left[0]+right[0], root.val+left[1]+right[1]]

            if root.val == currAvg[1]//currAvg[0]:
                res[0] += 1
        
            return currAvg
        
        res = [0]
        traverse(root, res)
        
        return res[0]