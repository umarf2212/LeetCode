class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        def isValid(i, j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                return False
            return True
        
        def dfs(i, j, curIslandArea):
            if not isValid(i, j):
                return
            
            # mark current cell as visited
            grid[i][j] = 0
            curIslandArea[0] += 1

            dfs(i-1, j, curIslandArea)
            dfs(i+1, j, curIslandArea)
            dfs(i, j-1, curIslandArea)
            dfs(i, j+1, curIslandArea)

        maxArea = 0
    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curIslandArea = [0]
                    dfs(i, j, curIslandArea)
                    maxArea = max(curIslandArea[0], maxArea)
        
        return maxArea


