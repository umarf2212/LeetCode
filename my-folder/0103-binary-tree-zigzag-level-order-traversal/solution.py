# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def traverse(self, s, res, level):
        if len(s) == 0: return
        stack = []
        result = []
        
        while s:
            temp = s.pop()            
            
            result.append(temp.val)
            
            if level%2 == 0:
                if temp.left: stack.append(temp.left)
                if temp.right: stack.append(temp.right)
            else:
                if temp.right: stack.append(temp.right)
                if temp.left: stack.append(temp.left)
        
        res.append(result)
        self.traverse(stack, res, level+1)
            
    
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        res = []
        self.traverse([root], res, 0)
        return res
