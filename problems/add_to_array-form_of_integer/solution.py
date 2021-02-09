class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        
        s = ''
        for j in A:
            s += str(j)
        
        ar = []
        Sum = str(int(s) + K)
        for i in Sum:
            ar.append(i)
            
        return ar
        
        
        # return [i for i in str(int(''.join([str(j) for j in A]))+K)]