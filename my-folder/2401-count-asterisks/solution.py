class Solution:
    def countAsterisks(self, s: str) -> int:
        
        open = False
        res = 0
        for ch in s:
            
            if ch == '|':
                open = not open
            
            if ch == '*' and not open:
                res += 1
        
        return res

