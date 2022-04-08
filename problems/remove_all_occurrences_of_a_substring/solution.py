class Solution:
    def removeOccurrences(self, st: str, part: str) -> str:
        
        s = ''
        lp = len(part)
        ls = 0
        for i in st:
            s += i
            ls += 1
            
            if ls >= lp:
                if s[ls-lp:] == part:
                    s = s[:ls-lp]
                    ls = len(s)
        
        return s