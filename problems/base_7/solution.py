class Solution:
    def convertToBase7(self, num: int) -> str:
        
        newNum = ''
        neg = True if num < 0 else False
        num = abs(num)
        while num >= 7:
            
            dm = divmod(num, 7) # (14, 2) -> (2, 0)
            newNum += str(dm[1])
            num = dm[0]
        
        newNum += str(num)
        
        return '-' + newNum[::-1] if neg else newNum[::-1]