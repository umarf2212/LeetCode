class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        n = len(grid)
        A = grid
        
        def fps(i, j):
            if i >= n: return 0
        
            if dp[i][j] != -1:
                return dp[i][j]
            
            ans = float('inf')
            for k in range(n):
                if k == j: continue
                ans = min(ans, A[i][k] + fps(i+1, k) )
            
            dp[i][j] = ans
            return ans
        
        dp = [[-1 for _ in range(n)] for _ in range(n)]

        ans = float('inf')
        for j in range(n):
            ans = min(ans, A[0][j] + fps(1, j) )
        
        return ans
            

