# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None
        
        # One naive method is to copy to a new array, 
        # rotate array and copy back values.

        # Let's go with constant space method. 

        n = 0
        cur = head
        tail = head
        while cur:
            n += 1
            tail = cur
            cur = cur.next
        
        k = k % n

        # edge cases:
        if not head.next or k == 0:
            return head

        # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7

        i = 1
        cur = head
        while i < n-k:
            i += 1
            cur = cur.next
        
        newHead = cur.next
        cur.next = None

        tail.next = head

        return newHead

