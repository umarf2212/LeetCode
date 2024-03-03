class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = len(s)
        n = len(p)
        
        def rem(i, j):
            if j == n:
                return i == m
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            ans = False
            if i < m and (s[i]==p[j] or p[j]=='.'):
                ans = True
            
            if j+1 < n and p[j+1] == '*':
                ans = rem(i, j+2) or ans and rem(i+1, j)
            else:
                ans = ans and rem(i+1, j+1)
            
            dp[i][j] = ans
            return ans
        
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
        return rem(0, 0)

            

