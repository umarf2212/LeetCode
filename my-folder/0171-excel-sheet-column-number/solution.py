class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        d = {alpha[i]:i+1 for i in range(len(alpha))}
        n = len(columnTitle)
        
        res = 0
        for i in range(n):
            res += 26**(n-i-1) * (d[columnTitle[i]])
        
        return res
