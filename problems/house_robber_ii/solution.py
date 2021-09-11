class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        
        def findMaxMoney(nums):
            n = len(nums)
            dp = [0 for _ in range(n)]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max( dp[i-1] , nums[i] + dp[i-2] )
            
            return dp[n-1]
        
        sol1 = findMaxMoney(nums[:len(nums)-1])
        sol2 = findMaxMoney(nums[::-1][:len(nums)-1])
        
        return max(sol1, sol2)