class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        largest = float('-inf')
        largestIndex = 0
        
        for i in range(len(nums)):
            if nums[i] > largest:
                largest = nums[i]
                largestIndex = i
        
        for i in range(len(nums)):
            if nums[i] != largest and largest < nums[i]*2:
                return -1

        return largestIndex