class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        res = []
        for num in range(left, right+1):
            
            for digit in str(num):
                if digit == '0': break
                    
                if num % int(digit) != 0:
                    break
            else:
                res.append(num)
        
        return res
