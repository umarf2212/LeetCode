class Solution:
    
    @cache
    def steps(self, n):
        if n <= 3: return n 
        return self.steps(n-1) + self.steps(n-2)
    
    def climbStairs(self, n: int) -> int:
            
        return self.steps(n)
