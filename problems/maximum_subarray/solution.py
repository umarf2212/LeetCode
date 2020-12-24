class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 0: return 0
        
        max_so_far = nums[0]
        max_ends_here = nums[0]
        
        for i in range(1,len(nums)):
            
            max_ends_here = max(nums[i], max_ends_here+nums[i])
            max_so_far = max(max_so_far, max_ends_here)
        
        return max_so_far