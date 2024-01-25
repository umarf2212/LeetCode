# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists: return None

        # [1,2 ,7, 2,21 ,6]

        # 1 -> | 2 -> 4
        #        3 -> 5 -> 6

        def merge(l1, l2):
            if not l1: return l2
            if not l2: return l1

            if l1.val < l2.val:
                l1.next = merge(l1.next, l2)
                return l1
            else:
                l2.next = merge(l1, l2.next)
                return l2
        
        pq = [(ll.val, i, id(ll), ll) for i, ll in enumerate(lists) if ll]
        heapq.heapify(pq)

        while len(pq) >= 2:
            _, i, _, l1 = heapq.heappop(pq)
            _, j, _, l2 = heapq.heappop(pq)
            l3 = merge(l1, l2)
            heapq.heappush(pq, (l3.val, i+j, id(l3), l3))
        
        # print(pq)
        # print(pq[0][2])
        if not pq:
            return None

        return pq[0][3]

        

