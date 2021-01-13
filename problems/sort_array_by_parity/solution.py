class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        evenPos=0
        
        for i in range(len(A)):
            if A[i] % 2 == 0:
                A[evenPos], A[i] = A[i], A[evenPos]
                evenPos += 1
        
        return A