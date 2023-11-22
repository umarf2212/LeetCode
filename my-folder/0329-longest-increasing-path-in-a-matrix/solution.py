from collections import defaultdict
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        # build graph
        # do DFS on the graph with max path

        A = matrix
        m, n = len(A), len(A[0])

        def isValid(i, j):
            if i<0 or i>=m or j<0 or j>=n:
                return False
            return True
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        memo = [[1 for _ in range(n)] for _ in range(m)]
        def dfs(i, j):
            if memo[i][j] > 1:
                return memo[i][j]

            for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]

                    if isValid(x, y) and A[x][y] > A[i][j]:
                        memo[i][j] = max(memo[i][j], 1 + dfs(x, y))

            return memo[i][j]
        
        ans = -1
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j) )
        
        return ans

