# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:

        ar = []
        temp = head
        while temp:
            ar.append(temp.val)
            temp = temp.next


        # 2 7 4 3 5
        stack = []
        res = []
        for i in range(len(ar)-1,-1,-1):
            while stack and stack[-1] <= ar[i]:
                stack.pop()
            
            if not stack:
                res.append(0)
            else:
                res.append(stack[-1])
            
            stack.append(ar[i])
        
        return res[::-1]
