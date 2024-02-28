class Solution:
    def minInsertions(self, s: str) -> int:
        
        def lps(i, j):
            if i > j: return 0
            if i == j: return 1

            if dp[i][j] != -1:
                return dp[i][j]
        
            ans = -1
            if s[i] == s[j]:
                ans = 2 + lps(i+1, j-1)
            else:
                ans = max(lps(i+1, j), lps(i, j-1))
            
            dp[i][j] = ans
            return ans
        
        # Iterative
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]

        for i in range(n):
            dp[i][i] = 1
        
        for L in range(2, n+1):
            for i in range(n-L+1):
                j = i+L-1

                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        LPS = dp[0][n-1]
        
        # LPS = lps(0, n-1)

        return n-LPS

