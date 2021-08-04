class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        
        d = set([tuple(piece) for piece in pieces])

        ar = []
        for i in range(len(arr)):
            
            ar.append(arr[i])
            
            if tuple(ar) in d:
                ar = []
        
        return len(ar) == 0
