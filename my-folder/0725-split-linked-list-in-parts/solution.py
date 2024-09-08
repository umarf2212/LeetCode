# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        # Get the size n of the linked list
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        
        nodesPerPart = n//k
        extraNodeParts = n%k

        # returns two lists - 
        # head of first part removed and the rest of the list
        def divideList(head, size):
            count = 0
            temp = head
            while temp and count < size-1:
                count += 1
                temp = temp.next
            
            nextHead = None
            if temp:
                nextHead = temp.next
                temp.next = None

            return [head, nextHead]
        
        result = []
        temp = head
        while temp:
            size = nodesPerPart
            if extraNodeParts > 0:
                size += 1
                extraNodeParts -= 1
            
            res, temp = divideList(temp, size)
            result.append(res)

        if len(result) < k:
            result += [None] * (k - len(result))
        
        return result
