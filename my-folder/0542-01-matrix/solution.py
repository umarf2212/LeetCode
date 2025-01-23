from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        q = deque()

        m, n = len(mat), len(mat[0])

        dist = [[float('inf')] * n for _ in range(m)] 
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append( (i, j, 0) )
        
        def is_valid(i, j):
            if 0 <= i < m and 0 <= j < n and mat[i][j] == 1 and dist[i][j] == float('inf'):
                return True
            return False
        
        while q:
            i, j, d = q.popleft()

            for x, y in [(-1,0), (1,0), (0,-1), (0,1)]:
                new_i = i + x
                new_j = j + y

                if is_valid(new_i, new_j):
                    new_dist = d+1
                    dist[new_i][new_j] = min(dist[new_i][new_j], new_dist)
                    q.append( (new_i, new_j, new_dist) )
        
        return dist
