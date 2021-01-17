# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        ar = []
        temp = head
        
        while temp:
            ar.append(temp.val)
            temp = temp.next
        
        num = 0
        p = 0
        for i in range(len(ar)-1,-1,-1):
            num += ar[i] << p
            p+=1
        
        return num
