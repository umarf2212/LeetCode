class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # unnecessarily optimised code

        ops = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                s = nums[i-1] + 1
                ops += s - nums[i]
                nums[i] = s
        
        return ops
