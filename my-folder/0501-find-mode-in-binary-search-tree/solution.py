# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def find(self, root, d):
        if not root: return
        
        if root.val not in d:
            d[root.val] = 1
        else:
            d[root.val] += 1
        
        self.find(root.left, d)
        self.find(root.right, d)
    
    def findMode(self, root: TreeNode) -> List[int]:
        d = {}
        
        self.find(root, d)
        
        # print(d)
        
        max_c = float('-inf')
        res = []
        for num, count in d.items():
            if count > max_c:
                max_c = count
                res = [num]
            elif count == max_c:
                res.append(num)
        
        return res
