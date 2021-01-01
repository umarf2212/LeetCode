class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        if len(set(nums)) <= 2: return max(nums)
        
        max1 = max2 = max3 = float('-inf')
        
        for i in nums: max1 = i if i > max1 else max1
        for i in nums: max2 = i if i > max2 and i < max1 else max2
        for i in nums: max3 = i if i > max3 and i not in [max1, max2] else max3
            
                
        return max3
