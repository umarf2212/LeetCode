class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        elif rowIndex == 1: return [1,1]
        
        row = 2
        ar = [1,1]
        
        while row <= rowIndex:
            temp = []
            for i in range(len(ar)-1):
                temp.append(ar[i]+ar[i+1])
            
            ar = [1] + temp + [1]
            row += 1
        
        return ar