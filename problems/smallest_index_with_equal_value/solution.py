class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        
        res = len(nums)
        for i in range(len(nums)):
            if i % 10 == nums[i] and i < res:
                res = i
        
        if res == len(nums):
            return -1
        return res