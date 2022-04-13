class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        mat = [[0 for _ in range(n)] for _ in range(n)]
        
        offset = 0
        el = 1
        for i in range(n):
            
            #left to right
            for j in range(offset, n-offset):
                mat[i][j] = el
                el += 1
            
            #top to bottom
            for j in range(offset+1, n-offset):
                mat[j][n-1-i] = el
                el += 1
            
            # right to left
            for j in range(n-offset-2, offset-1, -1):
                mat[n-1-i][j] = el
                el += 1
            
            #bottom to top-1
            for j in range(n-offset-2, offset, -1):
                mat[j][i] = el
                el += 1
            
            #increase offset
            offset += 1
        
        return mat