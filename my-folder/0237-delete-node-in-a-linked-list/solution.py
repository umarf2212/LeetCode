# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        # 1. Whatever the given node is, just shift values of 
        #    subsequent nodes to this node and delete the last node.

        # 1 -> 2 -> 3 -> 4 -> N   |  Delete: 2
        # 1 -> _ -> 3 -> 4
        # 1 -> 3 -> _ -> 4
        # 1 -> 3 -> 4 -> _


        # O(N)
        temp = node
        prev = temp
        while temp.next:
            temp.val = temp.next.val
            prev = temp
            temp = temp.next
        
        prev.next = None
        

