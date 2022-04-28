class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def multiply(digit):
            result = ''
            carry = '0'
            
            for i in range(len(num1)-1, -1, -1):
                mul = str(int(num1[i]) * int(digit) + int(carry))
                
                carry = mul[0] if len(mul) > 1 else 0
                result += mul[1] if len(mul) > 1 else mul[0]
            
            if int(carry) > 0:
                result += str(carry)
                
            return result[::-1]
            
        # [738, 615, 492]
        result = 0
        for i in range(len(num2)-1, -1, -1):
            mul = int(multiply(num2[i]))
            result += mul * 10**(len(num2)-1-i)
            
        return str(result)