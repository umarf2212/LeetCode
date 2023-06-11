# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        # 1. Product is maximised only when both the multiplicands are maximised
        # 2. Hence both multiplicands can be maximum if abs diff between them is minimum

        mod = int(1e9+7)

        def findSum(root):
            nonlocal totalSum
            if not root: return

            totalSum += root.val 
            findSum(root.left)
            findSum(root.right)
        
        totalSum = 0
        findSum(root)

        def traverse(root):
            nonlocal minDiff
            nonlocal curSum
            nonlocal totalSum
            nonlocal ans
            if not root: return 0
            
            left = traverse(root.left) 
            right = traverse(root.right)

            curSum = (left + right + root.val) % mod

            a = curSum
            b = (totalSum - curSum)
            diff = abs(a-b)
            if diff < minDiff:
                minDiff = diff
                ans = [a, b]
            
            return curSum

        minDiff = float('inf')
        curSum = 0
        ans = -1
        traverse(root)
        return (ans[0] * ans[1]) % mod

