# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # N 1 -> 2 -> 3 -> N

        prev = None
        cur = head
        while cur:
            curNext = cur.next
            cur.next = prev
            prev = cur
            cur = curNext
        
        return prev
