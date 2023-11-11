class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        # Recurrence Relation:
        # dp[i][j] :-- 
        # if A[i] == A[j] : 2 + dp[i+1][j-1]
        # else max( dp[i+1][j], dp[i][j-1] )

        # (i, j) depends on => i+1 and j-1
        
        n = len(s)

        dp = [[0 for _ in range(n)] for _ in range(n)]

        # LPS of length 1 = 1
        for i in range(n):
            dp[i][i] = 1
        
        # for checking LPS of lens from 2 to n itself
        for length in range(2, n+1):
            for i in range(n - length + 1): # +1 cos it's upper limit
                j = i + length - 1 # -1 cos it's index

                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max( dp[i+1][j], dp[i][j-1] )
        
        return dp[0][n-1]

