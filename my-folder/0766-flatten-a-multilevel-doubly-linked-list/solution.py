"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    
    # 1 2 3 4  5 6
    # - - 7 8  9 10
    # - - - 11 12
    
    # - - 7 8 11 12 9 10
    
    # 1 2 3 7 8 11 12 9 10 4 5 6
    
    def flattened(self, head):
        
        temp = head
        while temp:
            
            tempNext = temp.next
            if temp.child:
                temp.next = self.flattened(temp.child)
                
                curr = temp
                while curr.next:
                    curr = curr.next
                
                curr.next = tempNext
                
                if tempNext:
                    tempNext.prev = curr
                
                temp.next.prev = temp
                
                temp.child = None
                
            temp = tempNext
            
        
        return head
    
    def flatten(self, head: 'Node') -> 'Node':
        return self.flattened(head)
