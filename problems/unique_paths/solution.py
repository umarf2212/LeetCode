class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # def paths(i, j):
        #     if i == 0 or j == 0:
        #         return 1
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     dp[i][j] = paths(i-1, j) + paths(i, j-1)

        #     return dp[i][j]
        

        # dp = [[-1 for _ in range(n)] for _ in range(m)]
        # return paths(m-1, n-1)

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            dp[i][0] = 1
        
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
