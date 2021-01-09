class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:        
        return [[row[col] for row in A] for col in range(len(A[0]))]