class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        if n == 1: return [0]
        
        ar = [] if n%2 == 0 else [0]
        
        for i in range(1, n//2 + 1):
            ar.append(i)
            ar.append(-i)
        
        return ar
