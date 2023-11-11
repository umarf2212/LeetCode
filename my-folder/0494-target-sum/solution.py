class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # Recurrence Relation

        # At every step, there are two options:
        # s + nums[i]
        # s - nums[i]

        # base case = i < 0 and s == target
        
        def sumWays(i, s):
            if i < 0:
                return 1 if s==target else 0
            
            if (i, s) in dp:
                return dp[i, s]
            
            dp[i, s] = sumWays(i-1, s + nums[i]) + sumWays(i-1, s-nums[i])
            return dp[i, s]
        
        n = len(nums)
        dp = {}

        return sumWays(n-1, 0)

        print(dp)

