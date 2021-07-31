class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        Sum = 0
        for d in str(n):
            product *= int(d)
            Sum += int(d)
        
        
        return product-Sum
