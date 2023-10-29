class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        m, n = max(m, n), min(m, n)
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp = [0 for _ in range(n)]

        # dp[0][0] = 1
        dp[0] = 1

        # for i in range(1, m):
        #     dp[i][0] = 1
        
        for j in range(1, n):
            dp[j] = 1
        
        for i in range(1, m):
            curRow = [1]
            for j in range(1, n):
                curRow.append(curRow[-1] + dp[j])
            
            dp = [i for i in curRow]

        return dp[-1]


