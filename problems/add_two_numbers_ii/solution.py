# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def populateStack(self, l1):
        stack = []
        
        temp = l1
        while temp:
            stack.append(temp.val)
            temp = temp.next
        
        return stack
        
    def buildLinkedList(self, stack1, stack2, carry):
        if not stack1 and not stack2: 
            if carry > 0:
                return ListNode(1)
            return None
        
        Sum = carry
        
        if stack1:
            Sum += stack1.pop()
        
        if stack2:
            Sum += stack2.pop()
        
        carry = 1 if Sum > 9 else 0
        newNode = ListNode(Sum % 10)
        
        newNode.next = self.buildLinkedList(stack1, stack2, carry)
        
        return newNode
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        stack1 = self.populateStack(l1)
        stack2 = self.populateStack(l2)
        
        # [7,2,4,3]
        # [-,5,6,4]

        head = self.buildLinkedList(stack1, stack2, 0)
        
        # 7->0->8<-7
        # 7->None
        
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev