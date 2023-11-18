class Solution:
    def countSubstrings(self, s: str) -> int:

        # Recurrence Relation
        # isP(i, j) = s[i] == s[j] and isP(i+1, j-1)
        
        # def isP(i, j):
        #     if i > j:
        #         return True
            
        #     if dp[i][j]:
        #         return True
            
        #     dp[i][j] = s[i] == s[j] and isP(i+1, j-1)
        #     return dp[i][j]
        
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(i+1):
                dp[i][j] = True
        
        for i in range(n-1):
            j = i+1
            if s[i] == s[j]:
                dp[i][j] = True

        for L in range(3, n+1):
            for i in range(n-L+1):
                j = i+L-1
                dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
        
        count = 0
        for i in range(n):
            for j in range(i, n):
                if dp[i][j]:
                    count += 1
        
        return count
            

