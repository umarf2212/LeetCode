class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1

        n = len(nums)
        
        lo = 0
        hi = n-1
        while lo <= hi:
            mid = (lo+hi) // 2

            # left extreme
            if mid == 0 and nums[0] > nums[1]:
                return mid
            
            # right extreme
            if mid == n-1 and nums[n-1] > nums[n-2]:
                return mid


            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid

            if nums[mid] > nums[mid+1]:
                hi = mid
            else:
                lo = mid+1
            

