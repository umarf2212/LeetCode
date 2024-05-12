class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        def calculateLargest(i, j, grid):
            Max = float('-inf')
            Max = max(Max, grid[i][j])
            Max = max(Max, grid[i-1][j-1])
            Max = max(Max, grid[i-1][j+1])
            Max = max(Max, grid[i+1][j-1])
            Max = max(Max, grid[i+1][j+1])
            Max = max(Max, grid[i+1][j])
            Max = max(Max, grid[i-1][j])
            Max = max(Max, grid[i][j+1])
            Max = max(Max, grid[i][j-1])
            return Max
        
        n = len(grid)

        result = []
        for i in range(1, n-1):
            row = []
            for j in range(1, n-1):
                row.append( calculateLargest(i, j, grid) )
            result.append(row)
        
        return result

