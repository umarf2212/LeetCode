class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
        m, n = len(matrix), len(matrix[0])
        
        maxCols = [-2 for _ in range(n)]
        
        ans = [[0 for _ in range(n)] for _ in range(m)]
        
        for j in range(n):
            for i in range(m):
                ans[i][j] = matrix[i][j]
                maxCols[j] = max(maxCols[j], matrix[i][j])
        
        for j in range(n):
            for i in range(m):
                if ans[i][j] == -1:
                    ans[i][j] = maxCols[j]
        
        return ans
        
