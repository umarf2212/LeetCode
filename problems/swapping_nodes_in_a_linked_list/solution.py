# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        temp = head
        ar = []
        while temp:
            ar.append(temp)
            temp = temp.next
        
        ar[k-1].val, ar[len(ar)-k].val = ar[len(ar)-k].val, ar[k-1].val
        
        return head