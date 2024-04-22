class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        
        # 1. Sort and compare

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1] != 1:
                return False
            
        return True
