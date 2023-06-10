class Solution:
    def isFascinating(self, n: int) -> bool:
        
        res = list(str(n) + str(2*n) + str(3*n))
        res.sort(key=lambda x:int(x))
        
        
        if len(res) > 9:
            return False
        
        for i in range(1, 10):
            if int(res[i-1]) != i:
                return False
        return True