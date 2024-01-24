# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def traverse(root, maxSumPath):
            if not root: return 0

            left = traverse(root.left, maxSumPath)
            right = traverse(root.right, maxSumPath)

            leftRightSum = left + root.val + right
            leftSum = left + root.val
            rightSum = right + root.val

            maxSumPath[0] = max(maxSumPath[0], leftRightSum, leftSum, rightSum, root.val)

            return max(leftSum, rightSum, root.val)
        
        maxSumPath = [root.val]
        
        traverse(root, maxSumPath)
        return maxSumPath[0]


