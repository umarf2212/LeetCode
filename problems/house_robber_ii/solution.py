class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])

        def ml(i, dp, A):
            if i < 0:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = max(ml(i-1, dp, A), A[i] + ml(i-2, dp, A))

            return dp[i]

        def maxLoot(A):
            n = len(A)
            dp = [-1] * n
            return ml(n-1, dp, A)
        
        return max( maxLoot(nums[1:]), maxLoot(nums[:-1]) )
            

        
