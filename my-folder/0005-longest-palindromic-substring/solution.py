class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        ans = s[0]

        for i in range(n):
            for j in range(i+1):
                dp[i][j] = True

        for i in range(n-1):
            j = i+1
            dp[i][j] = s[i] == s[j]
            
            if dp[i][j]:
                ans = s[i:j+1]
        
        for L in range(3, n+1):
            for i in range(n-L+1):
                j = i+L-1

                dp[i][j] = s[i] == s[j] and dp[i+1][j-1]

                if dp[i][j]:
                    ans = s[i:j+1]
        
        return ans

        def lps(i, j):
            if i > j:
                return True
            
            if dp[i][j]:
                return dp[i][j]
            
            dp[i][j] = s[i] == s[j] and lps(i+1, j-1)
            return dp[i][j]
