# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        tree = {}
        children = set()

        for p, c, isLeft in descriptions:
            children.add(c)

            if p not in tree:
                parent = TreeNode(p)
                tree[p] = parent
            else:
                parent = tree[p]
            
            if c not in tree:
                child = TreeNode(c)
                tree[c] = child
            else:
                child = tree[c]
            
            if isLeft:
                parent.left = child
            else:
                parent.right = child
        
        for num in tree.keys():
            if num not in children:
                return tree[num]
