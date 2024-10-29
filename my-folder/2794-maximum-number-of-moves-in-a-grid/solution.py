class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]

        def isValid(i, j, curVal):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] <= curVal:
                return False
            return True

        def moves(i, j):
            if j == n-1:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            

            maxMoves = 0

            if isValid(i-1, j+1, grid[i][j]):
                maxMoves = max(maxMoves, 1 + moves(i-1, j+1))
            
            if isValid(i, j+1, grid[i][j]):
                maxMoves = max(maxMoves, 1 + moves(i, j+1))
            
            if isValid(i+1, j+1, grid[i][j]):
                maxMoves = max(maxMoves, 1 + moves(i+1, j+1))

            dp[i][j] = maxMoves
            return maxMoves

        ans = 0
        for i in range(m):
            ans = max(ans, moves(i, 0))
        
        return ans

        # old thought process:

        # We can arrive at a cell (r, c) from =>
        #       (r+1, c-1)
        #       (r, c-1)
        #       (r-1, c-1)
        
        # maxMoves = 1 + max(moves(i-1, j+1), moves(i, j+1), moves(i+1, j+1))
