class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        
        for i in range(len(digits)-1, -1, -1):
            Sum = digits[i] + carry
            digits[i] = Sum % 10
            carry = 1 if Sum > 9 else 0
        
        return [1] + digits if carry==1 else digits
