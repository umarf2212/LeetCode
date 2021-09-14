class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        n = len(nums)
        
        k = sum(nums)
        if k%2 != 0: return False
        
        k = k//2
        
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        
        dp[0][0] = 1
        
        for i in range(1, n+1):
            for j in range(0, k+1):
                
                if j >= nums[i-1] and dp[i-1][j-nums[i-1]]:
                    dp[i][j] = dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][k]
