class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        validCells = 0
        start = [0,0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cell = grid[i][j]
                if cell == 1:
                    start = [i,j]
                
                if cell == 0:
                    validCells += 1

        def isValid(i, j, grid):
            if i in range(0, len(grid)) and j in range(0, len(grid[0])) and grid[i][j] not in [-1, 3]:
                return True
            return False
        
        def backtrack(grid, i, j, walks, pathCount):

            if grid[i][j] == 2:
                if pathCount-1 == validCells:
                    walks[0] += 1
                return
            
            grid[i][j] = 3

            if isValid(i-1, j, grid):
                backtrack(grid, i-1, j, walks, pathCount+1)
            
            if isValid(i+1, j, grid):
                backtrack(grid, i+1, j, walks, pathCount+1)
            
            if isValid(i, j-1, grid):
                backtrack(grid, i, j-1, walks, pathCount+1)
            
            if isValid(i, j+1, grid):
                backtrack(grid, i, j+1, walks, pathCount+1)
            
            grid[i][j] = 0

        

        walks = [0]
        i, j = start
        backtrack(grid, i, j, walks, 0)

        return walks[0]

