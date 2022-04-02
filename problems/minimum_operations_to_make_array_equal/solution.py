class Solution:
    def minOperations(self, n: int) -> int:
        
        m = n//2
        x = n//2 if n%2 == 0 else n//2+1
        return x*(2+(m-1)*2)//2