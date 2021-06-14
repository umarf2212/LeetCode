class Solution:
    def isHappy(self, n: int) -> bool:
        d = set()
        num = n
        while num not in d:
            d.add(num)
            num = sum([int(i)**2 for i in str(num)])
            if num == 1: return True
        
        return False