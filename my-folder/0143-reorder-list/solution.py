# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # 1 -> 2 -> 3

        # 1 -> 2 -> 3 -> 4 -> 5

        # N <- 1 <- 2 <- 3 <- 4

        # Efficient Approach:
        # 1. Find mid of list using slow-fast pointers
        # 2. Reverse the second half of the list
        # 3. Interleave the two lists formed
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # if fast is None, then even nodes
        # slow is the mid

        prev = None
        cur = slow
        while cur:
            curNext = cur.next
            cur.next = prev
            prev = cur
            cur = curNext
        
        # prev is the head of reversed list now

        # first list: head   -> ends on slow 
        # second list: prev  -> ends on None

        temp1 = head # ends on slow
        temp2 = prev # ends on None
        while temp1 != slow and temp2.next != None:
            temp1_next = temp1.next
            temp2_next = temp2.next

            temp1.next = temp2
            temp2.next = temp1_next

            temp1 = temp1_next
            temp2 = temp2_next


