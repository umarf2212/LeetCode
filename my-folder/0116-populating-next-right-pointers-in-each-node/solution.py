"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    
    def traverse(self, root):
        if not root: return
                
        if root.left:
            root.left.next = root.right
            root.right.next = root.next.left if root.next else None
        
        self.traverse(root.left)
        self.traverse(root.right)
    
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        
        self.traverse(root)
        
        return root
        
