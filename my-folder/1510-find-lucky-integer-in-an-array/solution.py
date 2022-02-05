class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        freq = Counter(arr)
        
        maxLucky = -1
        
        for num, count in freq.items():
            if num==count:
                if num > maxLucky:
                    maxLucky = num
        
        return maxLucky
