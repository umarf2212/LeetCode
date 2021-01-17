# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        d = {}
        
        temp = headA
        
        while temp:
            d[temp] = 0
            temp = temp.next
        
        temp = headB
        while temp:
            if temp in d:
                return temp
            temp = temp.next
        
        return None