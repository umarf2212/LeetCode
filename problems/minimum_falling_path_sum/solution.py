class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        A = matrix
        
        # def mfps(i, j):
        #     if i >= n: 
        #         return 0

        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     ans = float('inf')
            
        #     if j > 0:
        #         ans = min(ans, A[i][j] + mfps(i+1, j-1))
            
        #     ans = min(ans, A[i][j] + mfps(i+1, j))

        #     if j < n-1:
        #         ans = min(ans, A[i][j] + mfps(i+1, j+1))
            
        #     dp[i][j] = ans
        #     return ans
        
        dp = [-1 for _ in range(n)]

        for j in range(n):
            dp[j] = A[-1][j]
        
        for i in range(n-2, -1, -1):
            curRow = []
            for j in range(n):
                ans = float('inf')
                
                if j > 0:
                    ans = min(ans, A[i][j] + dp[j-1] )
                
                ans = min(ans, A[i][j] + dp[j])

                if j < n-1:
                    ans = min(ans, A[i][j] + dp[j+1])
            
                curRow.append(ans)
            
            dp = [i for i in curRow]


        # ans = float('inf')
        # for j in range(n):
        #     ans = min(ans, mfps(0, j))

        # print(dp)
        return min(dp)
