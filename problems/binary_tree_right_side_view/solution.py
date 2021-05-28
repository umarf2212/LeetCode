# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse_bfs(self, root):
        ar = []
        
        q = deque([[root, 0]])
        max_level = -1
        while q:
            curr = q.popleft()
            temp = curr[0]
            level = curr[1]
            #check level
            if level > max_level and temp:
                ar.append(temp.val)
                max_level += 1
            
            if temp: q.append([ temp.right, level+1 ])
            if temp: q.append([ temp.left, level+1 ])
        
        return ar

    
    def traverse(self, root, level, d):
        if not root: return
        
        #preorder
        if level not in d:
            d[level] = root.val
        
        right = self.traverse(root.right, level+1, d)
        left = self.traverse(root.left, level+1, d)
        
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        #bfs
        return self.traverse_bfs(root)
        
        d = {}
        self.traverse(root, 0, d)
        # print(d)
        return d.values()