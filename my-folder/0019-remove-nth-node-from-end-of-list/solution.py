# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        # length of the list is L
        # nth node from the end of list means -> (n-L+1)th node from first
        
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> N
        # 1 3, 2 4, 3 5, 4 6, 5 7
        
        # 1 -> 2
        # n = 1 or 2
        
        first = head
        second = head
        
        totalNodes = 1
        temp = head
        while temp.next:
            
            if totalNodes <= n:
                first = first.next
            
            temp = temp.next
            totalNodes += 1
        
        
        if totalNodes - n == 0:
            return head.next
                
        while first.next:
            first = first.next
            second = second.next
        
        # second -> n-1 th node
        second.next = second.next.next
        
        return head
        
