class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t: return False
        
        # i -> abc
        # j -> ahbgdc
        
        i = 0
        j = 0
        
        while i < len(s):
            
            if j == len(t) : return False
            
            if s[i] == t[j]:
                i += 1
            
            j += 1
            

            
        return True
