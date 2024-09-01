class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original): 
            return []

        
        result = []
        for j in range(0, m*n, n):
            result.append(original[j:j+n])
        
        return result
