class Solution:
    def fractionAddition(self, expression: str) -> str:

        def GCD(x , y):
            if y == 0:
                return x
            else:
                return GCD(y, x % y)

        def addFractions(f1, f2):
            f1 = list(map(int, f1.split('/')))
            f2 = list(map(int, f2.split('/')))

            numerator = (f1[0] * f2[1]) + (f1[1] * f2[0])
            denominator = f1[1] * f2[1]

            gcd = GCD(numerator, denominator)
            if gcd > 1:
                numerator = numerator // gcd
                denominator = denominator // gcd
            
            return str(numerator) + '/' + str(denominator)

        
        stack = []

        fractions = re.findall(r'-?\d+/\d+', expression)

        while len(fractions) > 1:
            f1 = fractions.pop()
            f2 = fractions.pop()

            fractions.append(addFractions(f1, f2))
        
        result = fractions[0]

        if result[0] == '0':
            return '0/1'
        
        return result


        # -24/3+8/2-4/2

        # -24, 3+8, 2-4, 1
