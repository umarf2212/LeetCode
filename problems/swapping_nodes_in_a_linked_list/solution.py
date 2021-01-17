# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        
        k_first = 0
        k_last = 0
        
        temp = head
        totalNodes = 0
        while temp:
            totalNodes += 1
            
            if totalNodes == k:
                k_first = temp
            
            temp = temp.next
            
        
        temp = head
        rev_count = 0
        while temp:
            rev_count += 1
            
            if rev_count == totalNodes - k + 1:
                prev_val = temp.val
                temp.val = k_first.val
                k_first.val = prev_val
                
                
            temp = temp.next
        
        return head