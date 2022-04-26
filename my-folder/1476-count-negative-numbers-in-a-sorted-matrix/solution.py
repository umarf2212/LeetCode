class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    count += 1
        return count
        
#         i = 0
#         j = len(grid[0])-1
        
#         count = 0
#         while i < len(grid)-1 and j > 0:
            
#             if grid[i][j] < 0:
#                 print(grid[i][j])
#                 count += (len(grid[0]) - j) + i
            
#             if grid[i+1][j] < grid[i][j-1]:
#                 i+=1
            
#             else:
#                 j-=1
        
#         return count
