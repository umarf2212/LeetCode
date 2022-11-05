"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []

        prevLevel = [root]
        ans = []
        while prevLevel:
            curLevel = []
            nextLevel = []
            for i in prevLevel:
                curLevel.append(i.val)
                if i.children:
                    nextLevel += i.children
            
            ans.append(curLevel)
            prevLevel = nextLevel

        return ans