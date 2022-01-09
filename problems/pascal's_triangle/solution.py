class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 1: return [[1]]
        
        triangle = [[1], [1,1]]
        
        for _ in range(numRows-2):
            
            currRow = [1]
            
            for i in range(1, len(triangle[-1])):
                currRow.append(triangle[-1][i]+triangle[-1][i-1])
            
            currRow.append(1)
            
            triangle.append(currRow)
        
        return triangle