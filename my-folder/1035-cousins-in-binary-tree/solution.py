# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, root, x, y):
        
        q = deque([[root, 0, None]])
        level = 0
        x_Node = None
        y_Node = None
        while q:
            curr = q.popleft()
            parent = curr[2]
            level = curr[1]
            curr = curr[0]
            
            if curr.val == x:
                x_Node = [curr, level, parent]
            elif curr.val == y:
                y_Node = [curr, level, parent]
            
            if x_Node and y_Node:
                break
            
            if curr.left: q.append([curr.left, level+1, curr])
            if curr.right: q.append([curr.right, level+1, curr])
        
        return x_Node[1] == y_Node[1] and x_Node[2] != y_Node[2]

        
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        return self.traverse(root, x, y)
