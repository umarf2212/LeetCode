# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        while cur:
            
            temp = cur
            while temp.next and temp.next.val == cur.val:
                temp = temp.next
            temp = temp.next
            
            cur.next = temp
            
            if cur:
                cur = cur.next
        
        return head
