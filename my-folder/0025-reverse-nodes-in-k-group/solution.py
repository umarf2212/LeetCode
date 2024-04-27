# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # 1 -> 2 -> 3 -> 4 -> 5 -> 6
        
        # 1 -> 2 -> 3 | -> 4 -> 5 -> 6 |  -> 7 -> 8
        # k = 3

        # 2 -> 1

        # newHead, newTail, nextGroupPointer = reverseKNodes(head)
        # newTail.next = joinNodeGroup(nextGroupPointer)

        # 1

        # 2 -> 1 -> 4 -> 3 -> 6 -> 5

        # k = 2

        # N <- 1 <- 2 -> 3 -> 4 -> N
        # p c    n

        def reverseKNodes(head, k):
            if not head: return 

            temp = head
            nodeCount = 0
            while temp.next:
                temp = temp.next
                nodeCount += 1
            
            if nodeCount+1 < k:
                return (head, temp, None)

            cur = head
            prev = None
            while k > 0 and cur:
                curNext = cur.next
                cur.next = prev
                prev = cur
                cur = curNext
                k -= 1
            
            # prev: newHead
            # head: newTail

            return (prev, head, cur)
        
        def joinNodeGroup(head, k):
            if not head: return
            
            newHead, newTail, nextGroupPointer = reverseKNodes(head, k)
            newTail.next = joinNodeGroup(nextGroupPointer, k)

            return newHead
        
        return joinNodeGroup(head, k)



