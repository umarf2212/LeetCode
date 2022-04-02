# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if not head: return
        
        less = []
        more = []
        
        temp = head
        while temp:
            
            if temp.val < x:
                less.append(temp.val)
            else:
                more.append(temp.val)
            
            temp = temp.next
        
        less += more
        i=0
        temp = head
        while temp:
            temp.val = less[i]
            i+=1
            temp = temp.next
        
        return head
