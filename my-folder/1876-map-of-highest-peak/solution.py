from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        

        q = deque()

        m, n = len(isWater), len(isWater[0])

        height = [[float('-inf')] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    q.append( (i, j, 0) )

        def is_valid(i, j):
            if 0 <= i < m and 0 <= j < n and isWater[i][j] == 0 and height[i][j] == float('-inf'):
                return True
            return False
        
        while q:
            i, j, d = q.popleft()

            for x, y in [(-1,0), (1,0), (0,-1), (0,1)]:
                new_i = i + x
                new_j = j + y

                if is_valid(new_i, new_j):
                    new_height = d + 1
                    height[new_i][new_j] = max(height[new_i][new_j], new_height)
                    q.append( (new_i, new_j, new_height) )
    
        return height
