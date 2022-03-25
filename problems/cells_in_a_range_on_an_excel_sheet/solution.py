class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        
        res = []
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for c in range(alpha.index(s[0]), alpha.index(s[3])+1):
            for r in range(int(s[1]), int(s[4])+1):
                res.append( alpha[c]+str(r) )
        
        return res