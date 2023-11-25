class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # Recurrence Relation
        # f(i, j) = grid[i][j] + min(f(i-1, j), f(i, j-1))

        # Base Cases: 
        # First Cell: (0, 0) => grid[0][0]
        # First Row: (0, j) = grid[0][j] + grid[0][j-1]
        # First Col: (i, 0) = grid[i][0] + grid[i-1][0]

        # Recursive or Iterative

        m, n = len(grid), len(grid[0])

        # O(mn)
        # Space Complexity: O(mn)
        dp = [0 for _ in range(n)]

        # Base Cases:

        # first cell
        dp[0] = grid[0][0]

        # first col - O(m)
        for j in range(1, n):
            dp[j] = grid[0][j] + dp[j-1]
        
        # Fill the DP table in a Bottom-Up fashion - O(mn)
        for i in range(1, m):
            curRow = [-1 for _ in range(n)]
            curRow[0] = grid[i][0] + dp[0]
            for j in range(1, n):
                curRow[j] = grid[i][j] + min(dp[j], curRow[j-1])
            
            dp = curRow[:]
        
        return dp[n-1]


