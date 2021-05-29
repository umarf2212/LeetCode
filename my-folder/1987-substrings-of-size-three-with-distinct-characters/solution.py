class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        total = 0
        
        i = 0
        while i+2 < len(s):
            
            if s[i+2] == s[i+1] or s[i+2] == s[i] or s[i+1] == s[i]:
                i += 1
                continue
            else:
                total += 1
            
            i+=1
            
        return total
