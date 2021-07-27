class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        start = -1
        end = -1
        
        #first position
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low+high)//2
            
            if nums[mid] < target:
                low = mid+1
            elif nums[mid] > target:
                high = mid-1
            else:
                start = mid
                high -= 1
            
            
        
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low+high)//2
            
            if nums[mid] < target:
                low = mid+1
            elif nums[mid] > target:
                high = mid-1
            else:
                end = mid
                low += 1
            
        
        return [start, end]
