class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        def increment(row, col, mat): 
            for c in range(len(mat[0])):
                mat[row][c] += 1
            
            for r in range(len(mat)):
                mat[r][col] += 1
        
        mat = [[0 for _ in range(n)] for _ in range(m)]
        for op in indices:
            increment(op[0], op[1], mat)
        
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] % 2 != 0:
                    res += 1
        
        return res
