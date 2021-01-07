class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        if len(nums) == 0: return 0
        
        currMax = 1
        maxSoFar = 1
        
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                currMax += 1
                maxSoFar = max(maxSoFar, currMax)
            else:
                currMax = 1
        
        return maxSoFar