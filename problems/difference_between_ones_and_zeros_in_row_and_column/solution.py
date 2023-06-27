class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        m = len(grid)
        n = len(grid[0])
        onesRow = [0 for _ in range(m)]
        onesCol = [0 for _ in range(n)]
        zerosRow = [0 for _ in range(m)]
        zerosCol = [0 for _ in range(n)]

        diff = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    onesRow[i] += 1
                    onesCol[j] += 1
                else:
                    zerosRow[i] += 1
                    zerosCol[j] += 1
        
        for i in range(m):
            for j in range(n):
                diff[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
        
        return diff