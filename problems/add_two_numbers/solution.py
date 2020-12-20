# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        digits = []
        p1 = l1
        p2 = l2
        while p1 or p2:
            theSum = 0
            if p1:
                theSum += p1.val
            if p2:
                theSum += p2.val
            if carry > 0:
                theSum += carry
                carry = 0
            
            if theSum >= 10:
                digits.append(theSum % 10)
                carry = 1
            else:
                digits.append(theSum)
            
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        
        if carry > 0:
            digits.append(1)
        
        # print(digits)
        head = ListNode(digits[0])
        ptr = head
        for el in digits[1:]:
            newNode = ListNode(el)
            ptr.next = newNode
            ptr = newNode
            
        return head
            