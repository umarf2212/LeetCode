# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        count = 1
        prev = head
        prev2 = head
        while prev:
            
            if count == m:
        
                curr = prev
                temp = None
                
                i = m
                while i <= n:
                    nextNode = curr.next
                    curr.next = temp
                    temp = curr
                    curr = nextNode
                    i += 1
                
                if m != 1:
                    prev2.next.next = curr
                    prev2.next = temp
                else:
                    head.next = curr
            
            prev2 = prev
            prev = prev.next
            count += 1
        
        return temp if m == 1 else head 