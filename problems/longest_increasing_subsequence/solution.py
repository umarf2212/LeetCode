class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        dp = [1 for _ in range(n)]
        
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):        
                if nums[i] < nums[j] and dp[i] < 1 + dp[j]:
                    dp[i] = 1 + dp[j]
        
        
        res = -1
        for i in range(n):
            if dp[i] > res:
                res = dp[i]
        
        return res