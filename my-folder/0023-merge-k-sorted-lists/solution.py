# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    # [[], [], [], [], [], []]
    
    def merge(self, l1, l2):
        if not l1: return l2
        elif not l2: return l1
        
        smaller = l1 if l1.val <= l2.val else l2
        larger = l1 if l1.val > l2.val else l2
        
        smaller.next = self.merge(smaller.next, larger)
        return smaller
    
    def divide(self, lists):
        
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        
        
        mid = len(lists)//2
        list1 = self.divide(lists[:mid])
        list2 = self.divide(lists[mid:])
        
        return self.merge(list1, list2)
        
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self.divide(lists)
