# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        temp = head
        ar = []
        while temp:
            ar.append(temp.val)
            temp = temp.next
        
        ar.sort()
        
        temp = head
        c = 0
        while temp:
            temp.val = ar[c]
            c += 1
            temp = temp.next
        
        return head
