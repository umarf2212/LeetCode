class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] *= -1
        
        nums.sort()
        
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        
        return nums
