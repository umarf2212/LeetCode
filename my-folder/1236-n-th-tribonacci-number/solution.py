class Solution:
    def tribonacci(self, n: int) -> int:
        
        first = 0
        second = 1 
        third = 1
        
        if n < 3: return [first, second, third][n]
        
        for _ in range(3, n+1):
            fourth = first + second + third
            first = second
            second = third
            third = fourth
            
        return third
