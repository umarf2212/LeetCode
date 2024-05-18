# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        def getHeight(root):
            if not root: return 0
            return 1 + max(getHeight(root.left), getHeight(root.right))
        
        height = getHeight(root) - 1
        m = height + 1
        n = 2**m - 1

        matrix = [["" for _ in range(n)] for _ in range(m)]

        # place root node
        # matrix[0][(n-1)//2] = str(root.val)

        def dfs(root, r, c, matrix, height):
            if not root: return

            matrix[r][c] = str(root.val)
            print(r, c)

            dfs(root.left, r+1, c-2**(height-r-1), matrix, height)
            dfs(root.right, r+1, c+2**(height-r-1), matrix, height)
        
        dfs(root, 0, (n-1)//2, matrix, height)

        return matrix
