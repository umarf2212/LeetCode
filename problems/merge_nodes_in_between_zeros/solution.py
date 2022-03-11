# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        head = head.next
        temp = head
        while temp:
            currSum = 0
            curr = temp
            while temp.val != 0:
                currSum += temp.val
                temp = temp.next
            
            temp = temp.next
            curr.val = currSum
            curr.next = temp
        
        return head