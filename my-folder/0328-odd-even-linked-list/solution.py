# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        

        headOdd = head
        headEven = head.next

        # 1 -> 2 -> 3 -> 4 -> N
        # 1 -> 3
        # 2 -> 4

        # 1 -> 2 -> 3 -> N
        # 1 -> 3
        # 2 -> N

        odd = headOdd
        even = headEven
        while even and even.next:
            odd.next = even.next
            even.next = even.next.next

            odd = odd.next
            even = even.next
        
        odd.next = headEven

        return headOdd

