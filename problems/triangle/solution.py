class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        A = triangle
        
        # Recurrence relation:
        # msp(i, j) = A[i][j] + min( msp(i-1, j), msp(i-1, j-1) )
        # for all j in A[-1]

        def msp(i, j):

            if i == 0 and j == 0:
                return A[0][0]
            
            if j < 0 or j >= len(A[i]):
                return float('inf')
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            ans = A[i][j] + min( msp(i-1, j), msp(i-1, j-1) )
            dp[i][j] = ans
            return ans
        
        m, n = len(A), len(A[-1])

        # dp = [[-1 for _ in range(n)] for _ in range(m)]

        dp = []
        for i in range(m):
            dp.append( [-1] * len(A[i]) )

        ans = float('inf')
        for j in range(len(A[-1])):
            ans = min(ans, msp(m-1, j))
        
        return ans


