class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        if len(nums) == 0: return 1
        
        d = {}
        
        Max = float('-inf')
        for i in nums:
            d[i] = 0
            
            if i > Max:
                Max = i

        for i in range(1, Max):
            if i not in d:
                return i
            
        return Max+1 if Max > 0 else 1