class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        flat = [j for i in grid for j in i]
        
        k = len(flat) - k % len(flat)
        
        flat = flat[k:] + flat[:k]
        
        res = []
        cols = len(grid[0])
        for i in range(0, len(flat), cols):
            res.append(flat[i:i+cols])
        
        return res
