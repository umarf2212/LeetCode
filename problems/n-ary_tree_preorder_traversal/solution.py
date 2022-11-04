"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        def traverse(root, ar):
            if not root: return

            ar.append(root.val)

            for child in root.children:
                traverse(child, ar)
        
        ar = []
        traverse(root, ar)
        return ar