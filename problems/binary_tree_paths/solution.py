# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def all_paths(self, root, curr_path, res):
        if not root: return
        
        curr_path.append(root.val)
        
        if not root.left and not root.right:
            res.append(list(curr_path))
        else:
            self.all_paths(root.left, curr_path, res)
            self.all_paths(root.right, curr_path, res)
        
        curr_path.pop()
    
    def make_str(self, ar):
        s=''
        for i in range(len(ar)-1):
            s += str(ar[i]) + '->'
        s+=str(ar[-1])
        return s
    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        
        res = []
        self.all_paths(root, [], res)
        res = [self.make_str(ar) for ar in res]
        return res