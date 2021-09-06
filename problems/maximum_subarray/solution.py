class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxNegative = float('-inf')
        for i in range(len(nums)):
            if nums[i] > maxNegative:
                maxNegative = nums[i]
            
            if nums[i] > 0:
                break
        
        if i == len(nums)-1 and nums[i] < 0:
            return maxNegative
        
        sumSoFar = 0
        maxSum = 0
        
        for i in range(len(nums)):
            
            if sumSoFar + nums[i] > 0:
                sumSoFar += nums[i]
            else:
                sumSoFar = 0
            
            if sumSoFar > maxSum:
                maxSum = sumSoFar
        
        return maxSum