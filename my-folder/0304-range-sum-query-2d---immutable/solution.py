class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m, n = len(matrix), len(matrix[0])
        self.prefixMat = [[0]*n for _ in range(m)]

        self.prefixMat[0][0] = matrix[0][0]

        for j in range(1, n):
            self.prefixMat[0][j] = self.prefixMat[0][j-1] + self.matrix[0][j]
        
        for i in range(1, m):
            self.prefixMat[i][0] = self.prefixMat[i-1][0] + self.matrix[i][0]
        
        for i in range(1, m):
            for j in range(1, n):
                self.prefixMat[i][j] = self.prefixMat[i-1][j] + self.prefixMat[i][j-1] + self.matrix[i][j] - self.prefixMat[i-1][j-1]
        
        print(self.prefixMat)



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        res = self.prefixMat[row2][col2]

        if row1 > 0:
            res -= self.prefixMat[row1-1][col2]

        if col1 > 0:
            res -= self.prefixMat[row2][col1-1]
        
        if row1 > 0 and col1 > 0:
            res += self.prefixMat[row1-1][col1-1]

        return res



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
