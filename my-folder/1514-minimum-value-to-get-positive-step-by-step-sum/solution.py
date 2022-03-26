class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        # -3 2 -3 4 2
        # -3 -1 -4 0 2
        # 2  4   1 5 7
        
        prefixSum = nums[0]
        Min = prefixSum
        for i in range(1, len(nums)):
            prefixSum += nums[i]
            Min = min(prefixSum, Min)
        
        if Min < 0:
            return abs(Min)+1
        
        return 1
