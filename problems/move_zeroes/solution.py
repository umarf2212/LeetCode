class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        while start < len(nums) and nums[start] != 0:
            start += 1
            
        nonZero = start
        
        for i in range(start, len(nums)):
            
            while nonZero < len(nums) and nums[nonZero] == 0:
                nonZero += 1
            
            if nonZero == len(nums): break
                
            if nums[i] == 0 and i < nonZero:
                nums[i] = nums[nonZero]
                nums[nonZero] = 0
        
        