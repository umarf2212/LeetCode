class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        res = ''
        carry = 0
        
        small = num1[::-1] if len(num1) < len(num2) else num2[::-1]
        big = num1[::-1] if len(num1) > len(num2) else num2[::-1]
        
        if len(num1) == len(num2):
            small = num1[::-1]
            big = num2[::-1]
        
        for i in range(len(big)):
            s = 0
            if i < len(small):
                s += int(small[i])
            if i < len(big):
                s += int(big[i])
            s += int(carry)
            s = str(s)
            res += s[0] if len(s) == 1 else s[1]
            carry = 0 if len(s)==1 else 1
        
        if carry == 1:
            res += '1'
            
        return res[::-1]