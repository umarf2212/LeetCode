from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        q = deque()

        m, n = len(mat), len(mat[0])

        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append( (i, j, 0) )
        
        def isValid(i, j):
            if 0 <= i < m and 0 <= j < n and mat[i][j] == 1 and dist[i][j] == float('inf'):
                return True
            return False

    
        while q:
            i, j, d = q.popleft()

            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ix = i + x
                jy = j + y

                if isValid(ix, jy):
                    new_dist = d+1
                    dist[ix][jy] = min( dist[ix][jy], new_dist )
                    q.append((ix, jy, new_dist))
        
        return dist



        # 0 0 0 
        # 1 0 1
        # 1 1 1 

        # For every 0 cell, the dist is 0
        # Start BFS from every 0 cell and when 1 cell is reached,
        # update its distance with min
