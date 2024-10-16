class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])
        
        def isValid(i, j):
            if (i < 0 or i >= m) or (j < 0 or j >= n):
                return False
            return True

        memo = [[-1]*n for _ in range(m)]

        def dfs(i, j):
            if not isValid(i, j):
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]
                
            ans = 0
            if isValid(i-1, j) and matrix[i-1][j] > matrix[i][j]:
                ans = max(ans, dfs(i-1, j))
            
            if isValid(i+1, j) and matrix[i+1][j] > matrix[i][j]:
                ans = max(ans, dfs(i+1, j))
            
            if isValid(i, j-1) and matrix[i][j-1] > matrix[i][j]:
                ans = max(ans, dfs(i, j-1))
            
            if isValid(i, j+1) and matrix[i][j+1] > matrix[i][j]:
                ans = max(ans, dfs(i, j+1))
            
            memo[i][j] = ans + 1
            
            return ans + 1
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
            
        return ans
