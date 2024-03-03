# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = head
        count = 1
        while temp.next and count < n:
            temp = temp.next
            count += 1
        
        if not temp.next:
            return head.next
        
        cur = head
        prev = temp
        while temp.next:
            temp = temp.next
            prev = cur
            cur = cur.next
        
        prev.next = cur.next
        return head


