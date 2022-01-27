# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, root, ar):
        if not root: return
        
        self.traverse(root.left, ar)
        ar.append(root.val)
        self.traverse(root.right, ar)

    def merge(self, q1, q2):
        newAr = []
        
        while q1 and q2:
            if q1[0] < q2[0]:
                newAr.append(q1.popleft())
            else:
                newAr.append(q2.popleft())
        
        if q1:
            newAr += list(q1)
        elif q2:
            newAr += list(q2)
        
        return newAr
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        ar1 = deque()
        self.traverse(root1, ar1)
        
        ar2 = deque()
        self.traverse(root2, ar2)
        
        return self.merge(ar1, ar2)
