class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        a1, b1 = num1.split('+')
        a2, b2 = num2.split('+')
        
        a1 = int(a1)
        a2 = int(a2)
        b1 = int(b1[:len(b1)-1])
        b2 = int(b2[:len(b2)-1])

        t1 = a1*a2 - b1*b2
        t2 = a1*b2 + a2*b1
        
        return str(t1) + '+' + str(t2) + 'i'
        
        