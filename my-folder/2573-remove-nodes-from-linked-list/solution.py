# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. Reverse the LL
        # 2. Recurse down the list
        # 3. We either discard the current node, or take it
        # That depends on whether it's value is >= prev max number value
        # If current node >= prevMax.val : we update prevMax as well
        # 4. Reverse back and return

        # 8 -> 3 -> 13 -> 2 -> 5 -> N

        def reverseList(listHead):
            prev = None
            cur = listHead
            while cur:
                curNext = cur.next
                cur.next = prev
                prev = cur
                cur = curNext
            
            return prev
        
        # prev holds the new head at this point
        head = reverseList(head)

        def createList(prevNode, cur):
            if not cur: return None

            if cur.val >= prevNode.val:
                cur.next = createList(cur, cur.next)
            else:
                return createList(prevNode, cur.next)
            
            return cur

        # start = ListNode(float('-inf'))
        head.next = createList(head, head.next)

        return reverseList(head)

        

