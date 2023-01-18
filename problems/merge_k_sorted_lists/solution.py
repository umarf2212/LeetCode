# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


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
        
        def divide(lists):
            if not lists: return None
            if len(lists) == 1: return lists[0]

            mid = len(lists)//2

            list1 = divide(lists[:mid])
            list2 = divide(lists[mid:])

            return merge(list1, list2)
        
        return divide(lists)