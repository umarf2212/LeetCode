"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return

        temp = head
        while temp:
            newNode = Node(temp.val)

            tempNext = temp.next
            temp.next = newNode
            newNode.next = tempNext
        
            temp = temp.next.next
        
        temp = head
        while temp:
            tempNext = temp.next
            tempNext.random = temp.random.next if temp.random else None
            temp = temp.next.next
        
        newHead = head.next

        temp = head
        while temp:
            tempNext = temp.next

            temp.next = tempNext.next
            
            if temp.next:
                tempNext.next = tempNext.next.next

            temp = temp.next
        
        return newHead
    
        
        
