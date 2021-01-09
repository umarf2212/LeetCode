class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        return [[row[i]^1 for i in range(len(row)-1,-1,-1)] for row in A]