class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)
        n = len(text2)

        def lcs(i, j):
            if i < 0 or j < 0:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            ans = -1
            if text1[i] == text2[j]:
                ans = 1 + lcs(i-1, j-1)
            else:
                ans = max(lcs(i-1, j), lcs(i, j-1))
            
            dp[i][j] = ans
            return ans
        
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        return lcs(m-1, n-1)

            
