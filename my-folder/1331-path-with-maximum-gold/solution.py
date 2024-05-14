class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def backtrack(i, j, grid, curGoldAmt, maxGoldAmt):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                return
            
            originalGoldAmt = grid[i][j]
            grid[i][j] = 0

            newCurGoldAmt = curGoldAmt + originalGoldAmt
            maxGoldAmt[0] = max(maxGoldAmt[0], newCurGoldAmt)


            for dx, dy in dirs:
                n_i, n_j = dx + i, dy + j
                backtrack(n_i, n_j, grid, newCurGoldAmt, maxGoldAmt)
            
            grid[i][j] = originalGoldAmt

        
        maxGoldAmt = [0]
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    backtrack(i, j, grid, 0, maxGoldAmt)
        
        return maxGoldAmt[0]

