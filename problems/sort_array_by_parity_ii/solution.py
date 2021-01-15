class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
        # half are odd, half are even
        # if we just put even nos. at even indices,
        # it will automatically put odd nos. and odd indices.
        
        nextEven = 0
        nextOdd = 0
        i = 0
        res = []
        for _ in range(len(A)//2):
            
            while A[nextEven] % 2 != 0:
                nextEven += 1
            
            while A[nextOdd] % 2 == 0:
                nextOdd += 1
                
            res.append(A[nextEven])
            res.append(A[nextOdd])
            nextEven += 1
            nextOdd += 1
        
        return res