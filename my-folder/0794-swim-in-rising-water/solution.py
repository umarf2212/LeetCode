class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def isValid(i, j, grid, maxVal):
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] > maxVal or (i, j) in vis:
                return False
            return True

        def dfs(i, j, grid, maxVal):
            if i == n-1 and j == n-1:
                return True
            
            vis.add((i, j))
            
            for dx, dy in dirs:
                new_i = dx + i
                new_j = dy + j

                if isValid(new_i, new_j, grid, maxVal):
                    if dfs(new_i, new_j, grid, maxVal):
                        return True
            
            return False

        n = len(grid)
        
        maxElevation = float('-inf')
        for i in range(n):
            for j in range(n):
                maxElevation = max(maxElevation, grid[i][j])
        
        # Left is grid[0][0] cos that's where we start, and not 
        # min value in the grid.
        left = grid[0][0]
        right = maxElevation
        while left < right:
            vis = set()
            mid = (left+right)//2

            if dfs(0, 0, grid, mid):
                right = mid
            else:
                left = mid+1
    
        return left


