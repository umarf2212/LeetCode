class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        m, n = len(grid1), len(grid1[0])
        
        def dfs(i, j, isSubisland):
            if i<0 or i>=m or j<0 or j>=n or grid2[i][j] == 0:
                return
            
            if grid1[i][j] == 0:
                isSubisland[0] = False
            
            grid2[i][j] = 0
            
            dfs(i-1, j, isSubisland)
            dfs(i+1, j, isSubisland)
            dfs(i, j-1, isSubisland)
            dfs(i, j+1, isSubisland)
        
        subislands = 0
        for i in range(m):
            for j in range(n):

                if grid2[i][j] == 1:
                    isSubisland = [True]
                    dfs(i, j, isSubisland)

                    if isSubisland[0]:
                        subislands += 1
        
        return subislands

