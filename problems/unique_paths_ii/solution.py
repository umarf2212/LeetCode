class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        A = obstacleGrid

        if A[0][0] == 1: return 0

        # Iterative

        m = len(A)
        n = len(A[0])

        # dp = [[0 for _ in range(n)] for _ in range(m)]
        dp = [0 for _ in range(n)]

        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
        
        return dp[-1]

