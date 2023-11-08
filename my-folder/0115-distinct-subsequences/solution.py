class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def ds(i, j):
            if j < 0: return 1
            if i < 0: return 0

            if dp[i][j] != -1:
                return dp[i][j]
            
            ans = ds(i-1, j)

            if s[i] == t[j]:
                ans += ds(i-1, j-1)
            
            dp[i][j] = ans
            return ans
        
        m = len(s)
        n = len(t)

        dp = [[-1 for _ in range(n)] for _ in range(m)]

        return ds(m-1, n-1)
            
