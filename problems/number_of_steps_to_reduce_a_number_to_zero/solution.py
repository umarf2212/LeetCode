class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        c = 0
        while num > 0:
            res = divmod(num, 2)
            if res[1] == 1:
                num -= 1
            else:
                num //= 2
                num = res[0]
            c+=1
                
        return c