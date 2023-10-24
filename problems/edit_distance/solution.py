class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        if m == 0: return n
        if n == 0: return m
        
        def ed(i, j):
            if i == 0:
                return j
            
            if j == 0:
                return i
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            ans = float('inf')
            if word1[i-1] == word2[j-1]:
                ans = ed(i-1, j-1)
            else:
                ans = 1 + min( ed(i-1, j), ed(i, j-1), ed(i-1, j-1) )

            dp[i][j] = ans
            return ans

        # ed(m, n)
        
        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i
        
        for j in range(n+1):
            dp[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):

                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        

        return dp[m][n]
