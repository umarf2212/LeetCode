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
    
    def checkSubpath(self, head, root):
        if not head: return True
        if not root: return False
        
        if head.val != root.val:
            return False
        else:
            left = self.checkSubpath(head.next, root.left)
            right = self.checkSubpath(head.next, root.right)
        
        return left or right
            
    
    def traverse(self, head, root):
        if not root: return False
        
        ans = False
        left = False
        right = False
        if head.val == root.val:
            ans = self.checkSubpath(head, root)
        
        left = self.traverse(head, root.left)
        right = self.traverse(head, root.right)
        
        return ans or left or right
    
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        return self.traverse(head, root)
