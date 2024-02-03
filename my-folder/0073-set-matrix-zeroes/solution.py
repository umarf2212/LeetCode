class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        inf = float('inf')
        m, n = len(matrix), len(matrix[0])

        row = [0 for _ in range(m)]
        col = [0 for _ in range(n)]

        for i in range(m):
            for j in range(n):    
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        
        for i in range(m):
            if row[i]:
                for j in range(n):
                    matrix[i][j] = 0
        
        for j in range(n):
            if col[j]:
                for i in range(m):
                    matrix[i][j] = 0
                    
        
        

                

