# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, q, res):
        if len(q) == 0: return
        new_q = deque([])
        result = []
        
        while q:
            temp = q.popleft()            
            
            result.append(temp.val)
            
            if temp.left: new_q.append(temp.left)
            if temp.right: new_q.append(temp.right)
        
        res.append(result)
        self.traverse(new_q, res)
        
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        q = deque([root])
        res = []
        self.traverse(q,res)
        return res[::-1]