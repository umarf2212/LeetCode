# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #  999 * 2 = 1998
        
        #  9 -> 9 -> 9

        # 1. Reverse the Linked List
        # 2. Double the numbers and take a carry forward
        # 3. If the carry is 1 at the end, add a new node with 1

        # 5 * 2 = 10

        # mul = N * 2 + carry
        # if mul > 9: carry = 1
        # curr number = mul % 10 

        def reverseList(head):
            temp = head
            prev = None
            while temp:
                tempNext = temp.next
                temp.next = prev
                prev = temp
                temp = tempNext
            return prev
        
        # prev holds the new head

        newHead = reverseList(head)

        carry = 0
        cur = newHead
        prev = newHead
        while cur:
            curNum = cur.val

            mul = curNum * 2 + carry

            if carry == 1: carry = 0

            if mul > 9: carry = 1

            cur.val = mul % 10

            prev = cur
            cur = cur.next
        
        # prev holds the tail
        
        # if there is a carry, add new node for it
        if carry == 1:
            carryNode = ListNode(1)
            prev.next = carryNode
        
        return reverseList(newHead)


