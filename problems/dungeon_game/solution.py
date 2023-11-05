class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        def kmh(i, j):
            if i >= m or j >= n:
                return float('inf')
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            ans = min( kmh(i+1, j), kmh(i, j+1) ) - A[i][j]
            dp[i][j] = max(ans, 1)
            return dp[i][j]
        
        A = dungeon
        m, n = len(A), len(A[0])

        dp = [[-1 for _ in range(n)] for _ in range(m)]

        dp[m-1][n-1] = max(1 - A[m-1][n-1], 1)

        kmh(0,0)
        return dp[0][0]