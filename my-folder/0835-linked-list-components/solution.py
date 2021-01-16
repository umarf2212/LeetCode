# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        d = {i:0 for i in G}
        
        CC = 0
        ar = []
        
        temp = head
        while temp:
            
            if temp.val in d:
                ar.append(temp.val)
            
            elif len(ar) > 0:
                CC += 1 
                ar = []
            
            
            temp = temp.next
            
        if len(ar) > 0:
            CC += 1
            
        return CC
