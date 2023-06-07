class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        for row in grid:
            row.sort(reverse=True)
        
        Sum = 0
        for j in range(len(grid[0])):
            curMax = float('-inf')
            for i in range(len(grid)):
                curMax = max(curMax, grid[i][j])
            
            Sum += curMax
        
        return Sum
