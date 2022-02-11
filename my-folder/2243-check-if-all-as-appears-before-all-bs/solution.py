class Solution:
    def checkString(self, s: str) -> bool:
        
        B = False
        
        for ch in s:
            if ch=='b':
                B = True
            elif B:
                return False
        
        return True
