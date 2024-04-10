"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def dfs(root):
            if not root: return 0

            maxDepth = 0
            for child in root.children:
                maxDepth = max(maxDepth, dfs(child))
            
            maxDepth += 1
            return maxDepth
        
        return dfs(root)
