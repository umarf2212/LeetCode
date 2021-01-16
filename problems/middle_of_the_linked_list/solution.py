# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        slow = head
        fast = head
        
        while slow and fast:
            if fast.next:
                fast = fast.next.next
            else:
                break
            slow = slow.next
        
        return slow