from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        
        m, n = len(grid), len(grid[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        vis = [[False for _ in range(n)] for _ in range(m)]

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dist[i][j] = 0
                    q.append((i, j, 0))
                    vis[i][j] = True
            
        def isValid(i, j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0 or grid[i][j]==2 or vis[i][j]:
                return False
            return True
        

        while q:
            i, j, d = q.popleft()

            # dist[i][j] = d

            for dx, dy in dirs:
                new_i = dx + i
                new_j = dy + j

                if isValid(new_i, new_j):
                    new_d = min(d+1, dist[new_i][new_j])
                    vis[new_i][new_j] = True
                    dist[new_i][new_j] = new_d
                    q.append((new_i, new_j, new_d))
        
        ans = -1
        allRotten = True
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    allRotten = False

                if grid[i][j] == 1:
                    ans = max(ans, dist[i][j])
        
        if allRotten: return 0
        
        return ans if ans != float('inf') else -1

