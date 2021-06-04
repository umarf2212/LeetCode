# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def traverse(self, root, stack):
        if not root: return
        
        stack.append(root.val)
        
        if not root.left and not root.right:
            self.res += int(''.join([str(i) for i in stack]),2)
            # nos.append(list(stack))
        
        self.traverse(root.left, stack)
        self.traverse(root.right, stack)
        
        stack.pop()
    
    def sumRootToLeaf(self, root: TreeNode) -> int:
        stack = []
        self.traverse(root, stack)
        return self.res