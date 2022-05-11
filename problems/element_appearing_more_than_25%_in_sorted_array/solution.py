class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        d = Counter(arr)
        ratio = len(arr) / 4
    
        for num, count in d.items():
            if count > ratio:
                return num