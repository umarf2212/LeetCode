# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def merge(self, l1, l2):
        if not l1: return l2
        elif not l2: return l1
        
        # 1->2->3
        # 5->6->7
        
        smaller = l1 if l1.val <= l2.val else l2
        larger = l1 if l1.val > l2.val else l2
        
        smaller.next = self.merge(smaller.next, larger)        
        
        return smaller

        
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.merge(l1, l2)
