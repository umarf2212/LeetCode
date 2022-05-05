class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        d = {}
        for num in arr:
            if num not in d:
                d[num] = 0
            d[num] += 1
    
        for num, count in d.items():
            if count * 100 / len(arr) > 25:
                return num