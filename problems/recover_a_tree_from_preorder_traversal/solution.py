# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:

        topRoot = None
        stack = []
        l = 0
        for ch in range(len(traversal)):
            if traversal[ch] != '-':

                if ch > 0 and traversal[ch-1] != '-':
                     stack[-1].val = stack[-1].val * 10 + int(traversal[ch])
                     continue

                while stack and len(stack) != l:
                    stack.pop()
                
                if not stack:
                    root = TreeNode(int(traversal[ch]))
                    stack.append(root)
                    topRoot = root
                else:
                    curr = TreeNode(int(traversal[ch]))
                    root = stack[-1]
                    if not root.left:
                        root.left = curr
                    else:
                        root.right = curr
                
                    stack.append(curr)

                l = 0
            else:
                l += 1
        
        # while len(stack) != 1:
        #     stack.pop()
        
        return topRoot