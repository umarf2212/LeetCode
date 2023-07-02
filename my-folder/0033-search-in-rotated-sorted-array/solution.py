class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # 0 1 2 3 4 5 6 7 8
        # 3 4 5 6 7 8 0 1 2

        def pivotPoint(nums):
            i = 0
            j = len(nums)-1
            while i <= j:
                mid = (i+j) // 2

                # naive idea is to check if pivot is greater than both it's 
                # adjacent elements,
                # and intuitive idea is that since array is sorted, we only need 
                # to check if nums[mid] > nums[mid+1] to consider it pivot
                if mid == len(nums)-1 or nums[mid] > nums[mid+1]:
                    return mid
                
                if nums[mid] >= nums[i]:
                    i = mid + 1
                else:
                    j = mid - 1
        
        def binarySearch(nums, i, j, target):
            while i <= j:
                mid = i + (j-i) // 2

                if nums[mid] == target:
                    return mid
                
                if nums[mid] > target:
                    j = mid - 1
                else:
                    i = mid + 1
            return -1

        pivot = pivotPoint(nums)
        if nums[pivot] == target:
            return pivot

        left = binarySearch(nums, 0, pivot, target)
        right = binarySearch(nums, pivot+1, len(nums)-1, target)

        if left != -1:
            return left
        return right
                

