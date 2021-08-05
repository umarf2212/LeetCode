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
        
        if root.left and root.right:
            root.left.next = root.right
            
            temp = root.next
            while temp and not temp.left and not temp.right:
                temp = temp.next
            
            if temp:
                root.right.next = temp.left if temp.left else temp.right
            
        elif root.left or root.right and root.next:
            curr = root.left if root.left else root.right
            
            temp = root.next
            while temp and not temp.left and not temp.right:
                temp = temp.next
            
            if temp:
                curr.next = temp.left if temp.left else temp.right
        
        self.traverse(root.right)
        self.traverse(root.left)
    
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        
        self.traverse(root)
        return root
