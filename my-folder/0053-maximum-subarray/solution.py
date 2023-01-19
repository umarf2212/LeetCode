class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sumSoFar = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            sumSoFar = max(nums[i], sumSoFar + nums[i])
            maxSum = max(maxSum, sumSoFar)
        
        return maxSum
