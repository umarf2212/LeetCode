class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0: return []
        elif numRows == 1: return [[1]]
        elif numRows == 2: return [[1], [1,1]]
        
        ar = [1,1]
        row = 2 #starting number of rows
        L = [[1], [1,1]]
        
        while row < numRows:
            temp = []
            for i in range(len(ar) - 1):
                temp.append(ar[i]+ar[i+1])
            
            ar = [1] + temp + [1]
            L.append(ar)
            row += 1
        
        return L
