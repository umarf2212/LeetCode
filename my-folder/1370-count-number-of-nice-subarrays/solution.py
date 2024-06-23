from collections import defaultdict
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        nums = [1 if nums[i]%2 else 0 for i in range(len(nums))]

        # The rest of the code below copied from:
        # https://leetcode.com/problems/binary-subarrays-with-sum/submissions/1297786785

        prefixSumCount = defaultdict(int)

        # This is important because think about when there's a subarray
        # that starts from i=0 to i=n and has prefixSum == k
        prefixSumCount[0] = 1

        prefixSum = 0
        subArrayCount = 0 
        for i in range(len(nums)):
            prefixSum += nums[i]

            # if prefixSum - k in prefixSumCount:
            subArrayCount += prefixSumCount[prefixSum-k]
            
            prefixSumCount[prefixSum] += 1

        return subArrayCount

