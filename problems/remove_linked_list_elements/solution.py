# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        temp = head
        prev = head
        
        if not head: return head
        
        while temp:
            
            while temp and temp.val == val:
                prev.next = temp.next 
                temp = temp.next
                
            if not temp: break
                
            prev = temp
            temp = temp.next
        
        return head if head.val != val else head.next