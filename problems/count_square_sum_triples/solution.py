class Solution:
    def countTriples(self, n: int) -> int:
        
        count = 0
        for a in range(1, n):
            for b in range(1, a):
                num = (a*a + b*b)**(1/2)
                if num <= n and num%1 == 0:
                    count+=2
                
        return count