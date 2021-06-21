class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            n = True
            rev = int(str(abs(x))[::-1])
        else:
            n = False
            rev = int(str(x)[::-1])
        
        if rev > 2147483647 or rev < -2147483647:
            return 0
        
        return -(rev) if n else rev
