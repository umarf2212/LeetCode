class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # def ml(i):
        #     if i < 0:
        #         return 0
            
        #     if dp[i] != -1:
        #         return dp[i]
            
        #     dp[i] = max(ml(i-1), nums[i] + ml(i-2))

        #     return dp[i]
        
        n = len(nums)
        dp = [-1] * n

        # return ml(n-1)

        A = nums

        if len(A) == 1: return A[0]
        if len(A) == 2: return max(A[0], A[1])

        dp[0] = A[0]
        dp[1] = max(A[0], A[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], A[i]+dp[i-2])
        
        return dp[n-1]

