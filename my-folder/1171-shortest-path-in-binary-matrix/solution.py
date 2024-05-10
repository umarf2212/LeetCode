from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        # Simple BFS to find the shortest path

        if grid[0][0] == 1: return -1


        n = len(grid)
        inf = float('inf')

        # (i, j, length)
        dq = deque([ (0, 0, 1) ])
        grid[0][0] = -1

        lengths = [ [inf] * n for _ in range(n) ]

        dirs = [[1,0], [0,1], [-1,0], [0,-1], [1,1], [-1,-1], [1,-1], [-1,1]]

        def isValid(i, j):
            if i<0 or i>=n or j<0 or j>=n or grid[i][j] == 1:
                return False
            return True

        while dq:
            i, j, curLength = dq.popleft()

            if i == n-1 and j == n-1:
                return curLength

            for dx, dy in dirs:
                nI = dx + i
                nJ = dy + j

                if isValid(nI, nJ) and curLength+1 < lengths[nI][nJ]:
                    lengths[nI][nJ] = curLength+1
                    dq.append( (nI, nJ, curLength+1) )
        
        return -1

        '''
        [0, 0, 0, 1, 1]
        [1, 1, 0, 0, 1]
        [1, 1, 1, 0, 0]
        [1, 1, 1, 1, 0]
        [1, 1, 1, 1, 0]
        '''
