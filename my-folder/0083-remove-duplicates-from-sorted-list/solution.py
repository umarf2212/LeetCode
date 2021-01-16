# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head: return None
        
        temp = head
        
        while temp.next:
            if temp.next.val == temp.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return head
