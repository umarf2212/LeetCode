# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        def merge(list1, list2):
            if not list1: return list2
            if not list2: return list1

            if list1.val < list2.val:
                small = list1
                big = list2
            else:
                small = list2
                big = list1
            
            small.next = merge(small.next, big)
            return small
        
        return merge(list1, list2)
