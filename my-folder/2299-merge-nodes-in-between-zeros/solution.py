# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        
        # 0 -> 3 -> 1 -> 0 -> 4 -> 5 -> 2 -> 0

        def merge(curSum, node):
            if not node: 
                return
            
            if node.val != 0:
                curSum += node.val
                return merge(curSum, node.next)
            
            else:
                newNode = ListNode(curSum)
                newNode.next = merge(0, node.next)
                return newNode
        
        return merge(0, head.next)
            


