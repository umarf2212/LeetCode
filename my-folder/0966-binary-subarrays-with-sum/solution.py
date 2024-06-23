from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:


        prefixSumCount = defaultdict(int)

        # This is important because think about when there's a subarray
        # that starts from i=0 to i=n and has prefixSum == goal
        prefixSumCount[0] = 1

        prefixSum = 0
        subArrayCount = 0 
        for i in range(len(nums)):
            prefixSum += nums[i]

            # if prefixSum - goal in prefixSumCount:
            subArrayCount += prefixSumCount[prefixSum-goal]
            
            prefixSumCount[prefixSum] += 1

        return subArrayCount
