# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        if not head or not head.next:
            return [-1,-1]

        # The idea is to traverse the linked list and store 
        # the critical points position as index in an array.
        # Now the problem boils down to finding max and min abs
        # difference b/w any two of these critical point indices.
        
        criticalPoints = []
        i = 2
        cur = head.next
        prev = head
        while cur.next:
            if prev.val < cur.val and cur.val > cur.next.val:
                criticalPoints.append(i)
            
            elif prev.val > cur.val and cur.val < cur.next.val:
                criticalPoints.append(i)

            i += 1
            prev = cur
            cur = cur.next

        if len(criticalPoints) < 2:
            return [-1, -1]

        criticalPoints.sort()

        maxDiff = criticalPoints[-1] - criticalPoints[0]

        minDiff = float('inf')
        for i in range(len(criticalPoints)-1,0,-1):
            minDiff = min(minDiff, criticalPoints[i]-criticalPoints[i-1])

        return [minDiff, maxDiff]
