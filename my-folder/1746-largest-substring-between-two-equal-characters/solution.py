class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        
        d = {}
        
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]][1] = i
            else:
                d[s[i]] = [i, 0]
                
        maxLength = -1
        
        for ind in d.values():
            if len(ind) > 1:
                sub = ind[1]-ind[0]-1
                if sub > maxLength:
                    maxLength = sub
        
        return maxLength
            
