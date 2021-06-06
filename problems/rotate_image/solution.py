class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = 0
        n = len(matrix)
        #offset means removing certain numbers out of the main number
        for layer in range(n):
            first = layer
            last = n - 1 - layer
            
            for i in range(first, last):
                offset = i-first
                
                temp = matrix[first][i]
                matrix[first][i] = matrix[last-offset][first]
                matrix[last-offset][first] = matrix[last][last-offset]
                matrix[last][last-offset] = matrix[i][last]
                matrix[i][last] = temp
                