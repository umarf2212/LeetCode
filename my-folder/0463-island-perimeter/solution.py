class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        p = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1:
                    
                    #check if borders
                    if i == 0: p+=1
                    elif grid[i-1][j] == 0: p += 1
                        
                    if j==0: p+=1
                    elif grid[i][j-1] == 0: p += 1
                        
                    if i==len(grid)-1: p+=1
                    elif grid[i+1][j] == 0: p += 1
                        
                    if j == len(grid[0])-1: p+=1
                    elif grid[i][j+1] == 0: p += 1
        
        return p
