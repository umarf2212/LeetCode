# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        def GCD(a, b):
            if b == 0:
                return a
            return GCD(b, a % b)
        
        temp = head
        while temp.next:
            tempNext = temp.next

            gcd = GCD(temp.val, tempNext.val)
            newNode = ListNode(gcd)

            temp.next = newNode
            newNode.next = tempNext
            temp = tempNext
        
        return head


