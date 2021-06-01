# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, root, val):
        
        q = deque([root])
        val = root.val
        s = set()
        while q:
            curr = q.popleft()
            s.add(curr.val)
            
            if curr.left: q.append(curr.left)
            if curr.right: q.append(curr.right)
        
        return len(s) == 1
    
    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.traverse(root, root.val)