class Solution:
    def toLowerCase(self, s: str) -> str:
        
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        d = {alpha[i]:i for i in range(26)}
        
        small = 'abcdefghijklmnopqrstuvwxyz'
        
        res = ''
        for i in s:
            if i in d:
                res += small[d[i]]
            else:
                res += i
        
        
        return res
