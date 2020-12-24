class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
            
        for i in range(len(digits)-1,-1,-1):

            theSum = digits[i] + carry

            if theSum == 10:
                digits[i] = 0
                carry = 1
            else:
                digits[i] = theSum
                carry = 0
                break

            
        if carry == 1:
            digits = [1] + digits
                
        return digits
