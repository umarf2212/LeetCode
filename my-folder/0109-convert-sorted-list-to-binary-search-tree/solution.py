# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def makeBST(self, ar, left, right):
        if left > right: return None

        mid = left + (right-left)//2
        
        newNode = TreeNode(ar[mid])
        
        newNode.left = self.makeBST(ar, left, mid-1)
        newNode.right = self.makeBST(ar, mid+1, right)
        
        return newNode
    
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return None
        if not head.next: return TreeNode(head.val)
        
        ar = []
        temp = head
        while temp:
            ar.append(temp.val)
            temp = temp.next
        
        return self.makeBST(ar, 0, len(ar)-1)
