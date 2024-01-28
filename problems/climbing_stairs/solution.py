class Solution:
    def climbStairs(self, n: int) -> int:
        
        def waysToClimb(x):
            # Base Case
            if x <= 3: return x
            
            # Check if memoised
            if dp[x] != -1:
                return dp[x]
            
            # Calculate
            res = waysToClimb(x-1) + waysToClimb(x-2)

            # Store/memoise
            dp[x] = res

            # Return
            return res
        
        dp = [-1] * (n+1)
        return waysToClimb(n)