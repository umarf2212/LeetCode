class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        
        rowMax = [-1 for _ in range(n)]
        colMax = [-1 for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                
                if rowMax[i] < grid[i][j]:
                    rowMax[i] = grid[i][j]
                
                if colMax[i] < grid[j][i]:
                    colMax[i] = grid[j][i]
                
        res = 0
        for i in range(n):
            for j in range(n):
                small = rowMax[i] if rowMax[i] < colMax[j] else colMax[j]
                
                if grid[i][j] < small:
                    res += small - grid[i][j]

        return res
