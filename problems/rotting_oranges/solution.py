from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def isValid(i, j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == 2 or grid[i][j] == 0 or vis[i][j] == 1:
                return False
            return True
        
        m, n = len(grid), len(grid[0])

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        vis = [[0 for _ in range(n)] for _ in range(m)]

        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dist[i][j] = 0
                    q.append( (i, j, 0) )
                    vis[i][j] = 1
        
        while q:
            i, j, d = q.popleft()

            dist[i][j] = d

            for k in range(4):
                new_I = dx[k] + i
                new_J = dy[k] + j

                if isValid(new_I, new_J):
                    new_dist = min( dist[new_I][new_J], d+1 )
                    q.append( (new_I, new_J, new_dist) )
                    vis[new_I][new_J] = 1
        
        ans = -1
        allRotten = True
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(dist[i][j], ans)
                    allRotten = False
        
        if allRotten: return 0

        return ans if ans != float('inf') else -1        

        
