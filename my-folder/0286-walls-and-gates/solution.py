from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        INF = 2147483647
        m, n = len(rooms), len(rooms[0])
        dq = deque()
    
        def isValid(i, j):
            if 0 <= i < m and 0 <= j < n and rooms[i][j] == INF:
                return True
            return False
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    dq.append( (i, j) )
                
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while dq:
            i, j = dq.popleft()

            for dx, dy in dirs:
                new_i = i + dx
                new_j = j + dy

                if isValid(new_i, new_j):
                    rooms[new_i][new_j] = rooms[i][j] + 1
                    dq.append( (new_i, new_j) )
        
        return dist



            



