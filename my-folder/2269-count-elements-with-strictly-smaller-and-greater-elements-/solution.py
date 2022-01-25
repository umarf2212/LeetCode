class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        # 11, 7, 2, 15
        # 2, 7, 11, 15
        
        # -3 3 3 90
        # -3 3 3 3 3
                
        Min = float('inf')
        Max = float('-inf')
        for i in range(len(nums)):
            if nums[i] < Min: 
                Min = nums[i]
                
            if nums[i] > Max: 
                Max = nums[i]
        
        if Min == Max:
            return 0
        
        count_min = 0
        count_max = 0
        for i in range(len(nums)):
            if nums[i] == Min:
                count_min += 1
            
            elif nums[i] == Max:
                count_max += 1
        
        return len(nums) - count_min - count_max
