class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return 0
        
        sumAr = []
        sumSoFar = 0
        sumTotal = sum(nums)
        
        for i in range(len(nums)):
            sumSoFar += nums[i]
            if sumSoFar - nums[i] == sumTotal - sumSoFar:
                return i
        
        return -1
        