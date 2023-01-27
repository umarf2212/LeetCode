# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q = deque([[root, 0]])
        ans = []
        temp = []
        curLevel = 0
        while q:
            cur = q.popleft()
            root = cur[0]
            level = cur[1]

            if level != curLevel:
                ans.append(temp)
                temp = []
                curLevel = level

            temp.append(root.val)

            if root.left:
                q.append([root.left, level+1])
            
            if root.right:
                q.append([root.right, level+1])
        
        if temp:
            ans.append(temp)
        
        return ans
