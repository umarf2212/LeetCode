# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        
        # find middle node
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        # Reverse the list from middle (slow)
        prev = slow
        temp = slow.next
        slow.next = None
        while temp:
            tempNext = temp.next
            temp.next = prev
            prev = temp
            temp = tempNext
        
        # prev is the tail
        
        left = head
        right = prev
        
        while right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
        
        return True