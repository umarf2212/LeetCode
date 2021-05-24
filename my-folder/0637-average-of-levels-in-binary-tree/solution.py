# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, q, res, level):
        if len(q) == 0: return
        
        result = []
        while q and q[0][1] == level:
            temp = q.popleft()
            
            result.append(temp[0].val)
            
            if temp[0].left: q.append([temp[0].left, level+1])
            if temp[0].right: q.append([temp[0].right, level+1])
        
        res.append(result)
        self.traverse(q, res, level+1)
    
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return []
        
        q = deque([[root, 0]])
        res = []
        self.traverse(q, res, 0)
        return [float('{x:.5f}'.format(x=sum(i)/len(i))) for i in res]
