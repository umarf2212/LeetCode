from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def waysToClimb(n):
            if n <= 3:
                return n
            return waysToClimb(n-1) + waysToClimb(n-2)
        
        return waysToClimb(n)
        

