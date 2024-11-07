class Solution:
    def makeFancyString(self, s: str) -> str:

        if len(s) < 3:
            return s
        
        res = s[:2]
        for i in range(2, len(s)):
            if res[-1] == res[-2] and s[i] == res[-1]:
                continue

            res += s[i]
            
        return res

