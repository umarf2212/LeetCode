# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 6 5 3 1 8 7 2 4

        # Dummy Node makes managing head much easier
        # D -> N

        dummy = ListNode(float('-inf'))
        cur = head
        while cur:
            
            # save current next for further traversal
            curNext = cur.next

            # start from dummy(first) node to check for insertion
            prev = dummy
            while prev.next and prev.next.val < cur.val:
                prev = prev.next
            
            # prev.next.val > cur.val
            # insert between prev and prev.next
            cur.next = prev.next
            prev.next = cur
        
            cur = curNext
        
        return dummy.next






