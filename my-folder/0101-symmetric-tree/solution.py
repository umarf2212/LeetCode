# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def level_order(self, root, arr):
        q = deque([root])
        
        while q:
            curr = q.popleft()
            
            if not curr:
                arr.append(None)
                continue
                
            arr.append(curr.val)
            q.append(curr.left)
            q.append(curr.right)
    
    def level_order_rev(self, root, arr):
        q = deque([root])
        
        while q:
            curr = q.popleft()
            
            if not curr:
                arr.append(None)
                continue
                
            arr.append(curr.val)
            q.append(curr.right)
            q.append(curr.left)

    
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root.left and not root.right: return True
        
        left = []
        right = []
        
        self.level_order(root.left, left)
        self.level_order_rev(root.right, right)

        return left==right
        
        # return left==right
