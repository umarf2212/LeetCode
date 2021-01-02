class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        flat = [j for i in grid for j in i]
        
        matrix = []
        
        row = []
        count = 0
        i = len(flat) - k % len(flat)
        start = i
        while 1:
            if i == len(flat):
                i = 0
                
            row.append(flat[i])
            count += 1
            
            if count == len(grid[0]):
                matrix.append(row)
                row = []
                count = 0
            
            if i == start-1:
                break
                
            i += 1
        
        return matrix
