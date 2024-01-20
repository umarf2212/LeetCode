class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        
        minSum = float('inf')
        for i in range(1, len(nums)):
            for j in range(i+1, len(nums)):
                    minSum = min(minSum, nums[0]+nums[i]+nums[j])
        
        return minSum
            
