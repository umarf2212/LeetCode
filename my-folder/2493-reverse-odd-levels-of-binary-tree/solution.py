# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # avoided using dictionary 

        q = deque([ [root, 0] ])
        curLevel = 0
        curLevelNodes = []
        levels = []
        while q:
            node, level = q.popleft()
            
            if level != curLevel:
                levels.append(curLevelNodes)
                curLevelNodes = [node]
                curLevel = level
            else:
                curLevelNodes.append(node)
            
            if node.left:
                q.append([node.left, level+1])

            if node.right:
                q.append([node.right, level+1])

        # for the last level
        levels.append(curLevelNodes)

        for i in range(len(levels)):
            level = levels[i]
            if i % 2 != 0:
                
                stack = []
                for node in level:
                    stack.append(node.val)
                
                for node in level:
                    node.val = stack.pop()
        
        return root
        



