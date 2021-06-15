class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        
        diff = float('inf')
        for i in range(1, len(arr)):
            d = abs(arr[i] - arr[i-1])
            if d < diff:
                diff = d
        
        res = []
        
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i-1]) == diff:
                res.append([arr[i-1], arr[i]])
        
        return res