class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        m = len(s)
        
        dp = [[0 for _ in range(m+1)] for _ in range(m+1)]
                
        for i in range(1, m+1):
            for j in range(1, m+1):
                
                if s[i-1] == s[m-j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        
        return dp[m][m]
