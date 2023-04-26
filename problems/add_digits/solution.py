class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10: 
            return num
        
        Sum = 0
        while num > 0:
            Sum += num % 10
            num //= 10
        
        return self.addDigits(Sum)

