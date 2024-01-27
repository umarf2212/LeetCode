class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return min(nums)
        
        i = 0
        j = len(nums)-1
        while i <= j:
            mid = (i+j)//2

            if nums[mid] < nums[mid-1]:
                return nums[mid]

            if nums[mid] > nums[j]:
                i = mid+1
            else:
                j = mid-1
        
