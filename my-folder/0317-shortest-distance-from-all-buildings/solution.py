from collections import deque
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        
        # 1. From each empty land 0, start a BFS, calculating the distance traveled.
        # 2. When a house is reached, stop.

        # 0 - empty land
        # 1 - building
        # 2 - obstacle

        def bfs(i, j, grid, distances):
            vis = [[False] * len(grid[0]) for _ in range(len(grid))]
            vis[i][j] = True
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            q = deque([ [i, j, 0] ])
            while q:
                i, j, d = q.popleft()

                if grid[i][j] == 0:
                    distances[i][j][0] += d
                    distances[i][j][1] += 1

                for dx, dy in dirs:
                    nI, nJ = dx + i, dy + j

                    if 0<=nI<m and 0<=nJ<n:
                        if grid[nI][nJ] == 0 and not vis[nI][nJ]:
                            q.append( [nI, nJ, d+1] )
                            vis[nI][nJ] = True

        m, n = len(grid), len(grid[0])
        totalHouses = 0

        # [distanceTraveled, houseCount]
        distances = [[[0,0] for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    totalHouses += 1
                    bfs(i, j, grid, distances)
        
        minDistance = float('inf')
        for i in range(m):
            for j in range(n):
                if distances[i][j][1] == totalHouses:
                    minDistance = min(minDistance, distances[i][j][0])
        
        if minDistance == float('inf'):
            return -1
        
        return minDistance

                    


