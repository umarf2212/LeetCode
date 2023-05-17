# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: return
        if not head.next: return head

        def swap(head):
            if not head: return

            first = head
            second = head.next
            if second:
                third = head.next.next
            else:
                return first
            
            second.next = first
            first.next = swap(third)

            return second

        newHead = head.next
        swap(head)
        return newHead

        # dry run
        # 1 -> 2 -> N
        # 1 -> 2 -> 3 -> N
        # 1 <- 2  4 -> 3 -> N

        # 2 -> 1 - 3 -> N

        # 1 2 3 4 N
            
