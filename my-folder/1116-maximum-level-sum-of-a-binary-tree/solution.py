# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        q = deque([[root, 1]])
        curLevel = 1
        maxSum = float('-inf')
        curSum = 0
        maxLevel = -1
        while q:
            cur, level = q.popleft()

            if level > curLevel:
                if curSum > maxSum:
                    maxSum = curSum
                    maxLevel = curLevel
                curSum = cur.val
                curLevel = level
            else:
                curSum += cur.val
            
            if cur.left:
                q.append([cur.left, level+1])
            
            if cur.right:
                q.append([cur.right, level+1])
        
        if curSum > maxSum:
            return curLevel
        
        return maxLevel


            
        





