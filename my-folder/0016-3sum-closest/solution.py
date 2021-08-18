class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        # 18
        # 1 2 3 4 7 8 10
        # 13 -> 18-15=3
        
        # -4 -1 1 2
        
        nums.sort()
        diff = float('inf')
        closest = 0
        
        for i in range(len(nums)):
            
            j = i+1
            k = len(nums)-1
            
            while j < k:
                
                Sum = nums[i] + nums[j] + nums[k]
                if Sum == target: return Sum
                
                curr_diff = abs(target - Sum)
                
                if curr_diff < diff:
                    diff = curr_diff
                    
                    closest = Sum
                
                if Sum > target:
                    k -= 1
                else:
                    j += 1
            
        return closest
