class Solution:
    def countSegments(self, s: str) -> int:
        if not s: return 0
        S = s.split(" ")
        
        c = 0
        for i in S:
            if len(i)>0: 
                c+=1
        
        return c
