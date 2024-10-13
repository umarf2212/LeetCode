from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # Multi-source BFS from each rotten orange to 
        # find shortest distance to each fresh orange.
        # The max distance to any fresh orange is the 
        # min time it takes to rot all oranges.

        m, n = len(grid), len(grid[0])
        inf = float('inf')

        dist = [[inf for _ in range(n)] for _ in range(m)]

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    dist[i][j] = 0
        
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        while q:
            i, j, d = q.popleft()

            for dx, dy in dirs:
                nI = dx + i
                nJ = dy + j

                if 0 <= nI < m and 0 <= nJ < n:
                    if grid[nI][nJ] == 1:
                        newDist = d+1

                        if newDist < dist[nI][nJ]:
                            dist[nI][nJ] = newDist
                            q.append((nI, nJ, newDist))
                            grid[nI][nJ] = 2
        
        maxDist = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
                
                if dist[i][j] != inf:
                    maxDist = max(maxDist, dist[i][j])
        
        return maxDist


        
