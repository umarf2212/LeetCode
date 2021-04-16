class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        
        ar = []
        evenSum = 0
        
        for i in range(len(A)):
            if A[i] % 2 == 0:
                evenSum += A[i]
                
        
        for query in queries:
            
            # query[1] --> index
            # query[0] --> value
            
            if A[query[1]] % 2 == 0:
                evenSum -= A[query[1]]
                
            A[query[1]] += query[0]
            
            if A[query[1]] % 2 == 0:
                evenSum += A[query[1]]
            
            ar.append(evenSum)
        
        return ar