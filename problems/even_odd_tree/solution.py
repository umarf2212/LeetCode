# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        
        
        q = deque([[root, 0]])
        
        evenPrev = None
        oddPrev = None
        
        while q:
            temp = q.popleft()
            curr = temp[0]
            level = temp[1]
            
            if level % 2 == 0:
                
                if oddPrev and oddPrev >= curr.val or curr.val % 2 == 0:
                    return False
                
                evenPrev = None
                oddPrev = curr.val
            
            else:
                if evenPrev and evenPrev <= curr.val or curr.val % 2 != 0:
                    return False
                
                oddPrev = None
                evenPrev = curr.val
            
            if curr.left: q.append([curr.left, level+1])
            if curr.right: q.append([curr.right, level+1])
        
        return True