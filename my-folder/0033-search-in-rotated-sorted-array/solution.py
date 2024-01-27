class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        def findPivot(nums):
            i = 0
            j = len(nums)-1

            while i <= j:
                mid = (i+j) // 2

                if mid == len(nums)-1 or nums[mid] > nums[mid+1]:
                    return mid
                
                if nums[i] <= nums[mid]:
                    i = mid+1
                else:
                    j = mid-1
        
        def binarySearch(nums, target, lo, hi):
            while lo <= hi:
                mid = (lo+hi) // 2

                if nums[mid] == target:
                    return mid
                
                if nums[mid] < target:
                    lo = mid+1
                else:
                    hi = mid-1
            
            return -1
        
        pivot = findPivot(nums)
        print(pivot)

        left = binarySearch(nums, target, 0, pivot)
        right = binarySearch(nums, target, pivot+1, len(nums)-1)

        if left != -1:
            return left
        
        return right

