class Solution:
    def reverse(self, x: int) -> int:

        # 321
        
        MIN = -2**31
        MAX = 2**31-1
        
        sign = -1 if x < 0 else 1

        x *= sign

        res = 0
        while x > 0:
            res = (res * 10) + (x % 10)
            x = x//10
        
        finalNum = res * sign

        if finalNum < MIN or finalNum > MAX:
            return 0

        return finalNum
