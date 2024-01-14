class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curSum = nums[0]
        sumSoFar = nums[0]

        for i in range(1, len(nums)):

            # does current element increase the overall curSum?
            # or is it greater than the curSum in itself?
            curSum = max(nums[i], curSum + nums[i])

            # is the curSum the max we've seen so far?
            sumSoFar = max(sumSoFar, curSum)
        
        return sumSoFar
