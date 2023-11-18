class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)
        isP = [[False for _ in range(n)] for _ in range(n)]


        # str of len 1 and invalid states are True
        for i in range(n):
            for j in range(i+1):
                isP[i][j] = True
        
        # base case: str of len 2
        for i in range(n-1):
            j = i+1
            isP[i][j] = s[i] == s[j]
        
        # len >= 3 check if s[i to j] Palindrome or not
        for L in range(3, n+1):
            for i in range(n-L+1):
                j = i+L-1
                isP[i][j] = s[i] == s[j] and isP[i+1][j-1]

        
        # Find minimum partitions \U0001f447
        
        # store min cuts at i
        dp = [float('inf') for _ in range(n)]

        # base case 
        for j in range(n):
            if isP[0][j]:
                dp[j] = 0

        # min cuts at prefix ending at i
        for i in range(1, n):
            for j in range(1, i+1):
                if isP[j][i]:
                    dp[i] = min(dp[i], 1+dp[j-1])

        return dp[n-1]