# import sys
# sys.setrecursionlimit(10000)
class Solution:
    def numSquares(self, n: int) -> int:

        # Recursive approach
        def mns(n, dp):
            if n == 0: return 0

            if dp[n] != -1:
                return dp[n]
            
            ans = n
            for i in range( 1, int(n**0.5) + 1 ):
                ans = min(ans, 1 + mns( n-(i*i) , dp))
            
            dp[n] = ans

            return ans
        
        # to further optimise, we can store pre-calculated squares
        squares = [0]
        for i in range(1, int(n**0.5)+1):
            squares.append(i*i)
        
        dp = [n for _ in range(n+1)]

        # Iterative Approach
        dp[0] = 0
        for i in range(1, n+1):
            for k in range(1, int(i**0.5)+1):
                dp[i] = min( dp[i], 1 + dp[ i - squares[k] ] )
        
        return dp[n]

        # return mns(n, dp)