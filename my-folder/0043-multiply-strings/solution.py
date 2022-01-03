class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        # 123 * 456
        
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
        
        result = 0
        j = 0
        for i in range(len(num2)-1, -1, -1):
            result += int(multiply(num2[i]) + ('0' * j))
            j+=1
            
        return str(result)
