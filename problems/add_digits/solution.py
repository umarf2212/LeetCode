class Solution:
    def addDigits(self, num: int) -> int:
        
        num = str(num)
        
        while len(num) != 1:
            num = str(sum([int(i) for i in num]))
        
        return int(num)