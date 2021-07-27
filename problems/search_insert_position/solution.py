class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]: return 0
        if target > nums[len(nums)-1]: return len(nums)
        
        low = 0
        high = len(nums)-1
        res = 0
        
        while low <= high:
            mid = (low+high)//2
            midVal = nums[mid]
            
            if midVal == target:
                return mid
            
            #greatest lesser
            elif midVal < target:
                res = mid
                low = mid+1
            
            elif midVal > target:
                high = mid - 1
        
        return res + 1