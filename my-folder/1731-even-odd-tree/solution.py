# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        q = deque([(root, 0)])

        levels = defaultdict(list)
        while q:
            cur, level = q.popleft()

            levels[level].append(cur.val)

            if cur.left:
                q.append((cur.left, level+1))
            
            if cur.right:
                q.append((cur.right, level+1))
        
        levels = list(levels.values())
        for i in range(len(levels)):
            level = levels[i]
            print(level)

            # even level
            if i%2 == 0:
                if level[0]%2 == 0: return False
                for j in range(1, len(level)):
                    if level[j] <= level[j-1] or level[j]%2 == 0:
                        return False
            
            # odd level
            else:
                if level[0]%2 == 1: return False
                for j in range(1, len(level)):
                    if level[j] >= level[j-1] or level[j]%2 == 1:
                        return False
                    

        return True
        
