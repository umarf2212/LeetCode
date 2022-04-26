class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
        xy = 0
        rowMax = [-1 for _ in range(len(grid))]
        colMax = [-1 for _ in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0: 
                    xy += 1
                rowMax[i] = max(rowMax[i], grid[i][j])
                colMax[j] = max(colMax[j], grid[i][j])
        
        yz = 0
        for i in rowMax:
            yz += i
            
        xz = 0
        for i in colMax:
            xz += i
        
        return xy + yz + xz
