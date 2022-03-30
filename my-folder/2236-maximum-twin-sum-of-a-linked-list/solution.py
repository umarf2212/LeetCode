# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        ans = float('-inf')
        
        stack = []
        
        slow = head
        fast = head
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        while slow:
            currSum = slow.val + stack.pop()
            if currSum > ans:
                ans = currSum
            
            slow = slow.next
        
        return ans
