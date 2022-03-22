class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        
        ar = []
        
        for i in range(rows):
            for j in range(cols):
                ar.append([i, j, abs(i - rCenter)+abs(j-cCenter)])
        
        ar.sort(key=lambda x: x[2])
        
        res = [[coord[0], coord[1]] for coord in ar]
        
        return res
