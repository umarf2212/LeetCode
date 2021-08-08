class Solution:
    
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        # 1 1 2 3 3 4 4 
        # 0 1 2 3 4 5 6
        
        # 1 1 5 2 2 3 3 4 4
        
        # before single -> duplicate is on even
        # after single -> duplicate is on odd
                
        low = 0
        high = len(nums) - 1
        
        while low <= high:            
            mid = (low+high) // 2
            
            if low == high:
                return nums[low]
            
            if mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    low = mid + 2
                else:
                    high = mid - 1
            else:
                if nums[mid] == nums[mid-1]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return nums[low]
