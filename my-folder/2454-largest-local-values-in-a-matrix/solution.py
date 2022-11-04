class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        def checkLargest(mat, i, j):
            Max = float('-inf')
            Max = max(Max, mat[i][j])
            Max = max(Max, mat[i-1][j-1])
            Max = max(Max, mat[i-1][j])
            Max = max(Max, mat[i][j-1])
            Max = max(Max, mat[i+1][j+1])
            Max = max(Max, mat[i+1][j])
            Max = max(Max, mat[i][j+1])
            Max = max(Max, mat[i-1][j+1])
            Max = max(Max, mat[i+1][j-1])
            return Max
        
        n = len(grid)
        res = [[0 for _ in range(n-2)] for _ in range(n-2)]
        for i in range(1, n-1):
            for j in range(1, n-1):
                res[i-1][j-1] = checkLargest(grid, i, j)

        return res


