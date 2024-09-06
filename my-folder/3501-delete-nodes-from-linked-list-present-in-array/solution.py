# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        
        nums = set(nums)

        while head and head.val in nums:
            head = head.next
        
        prev = head
        cur = head.next
        while cur:
            if cur.val not in nums:
                prev.next = cur
                prev = cur

            cur = cur.next
        
        prev.next = None
        
        return head
