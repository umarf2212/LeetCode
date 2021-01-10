# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        curr = head
        temp = None
        while curr:
            nextNode = curr.next
            curr.next = temp
            temp = curr
            curr = nextNode
        
        return temp
            
