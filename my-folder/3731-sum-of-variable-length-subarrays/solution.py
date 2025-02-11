class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        # 1 4 2 8 5 7
        # 1 5 7 15 20 27
        
        prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            prefixSum.append( nums[i] + prefixSum[-1] )

        res = 0
        for i in range(len(nums)):
            start = max(0, i-nums[i])    
            if start > 0: 
                res += prefixSum[i] - prefixSum[start-1]
            else:
                res += prefixSum[i]
            
        return res

