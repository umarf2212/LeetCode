class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        # 1 1 2 4 5
        # 1 5 2 4 1
        # 0 0 4 3 7
        # 1 5 6 7 8
        
        
        # 1 1 2 4 1
        
        
        res = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                res += nums[i-1] + 1 - nums[i]
                nums[i] = nums[i-1] + 1
            
            elif nums[i] == nums[i-1]:
                res += 1
                nums[i] = nums[i-1] + 1
        
        return res