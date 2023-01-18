# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # 1 2 3 4 5 6 7 8

        temp = head
        c = 1
        while temp and c < n:
            temp = temp.next
            c += 1
        
        if not temp.next:
            return head.next
        
        last_nth = head
        prev = head
        while temp.next:
            temp = temp.next
            prev = last_nth
            last_nth = last_nth.next
        
        prev.next = prev.next.next

        return head