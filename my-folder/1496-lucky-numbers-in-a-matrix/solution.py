class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        # 3   7 8 
        # 9  11 13 
        # 15 16 17

        m, n = len(matrix), len(matrix[0])
        
        rowMin = [float('inf')] * m
        colMax = [float('-inf')] * n

        for i in range(m):
            for j in range(n):
                rowMin[i] = min(rowMin[i], matrix[i][j])
                colMax[j] = max(colMax[j], matrix[i][j])
            
        # print(rowMin)
        # print(colMax)

        luckyNumbers = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] ==  rowMin[i] and matrix[i][j] == colMax[j]:
                    luckyNumbers.append(matrix[i][j])
        
        return luckyNumbers

