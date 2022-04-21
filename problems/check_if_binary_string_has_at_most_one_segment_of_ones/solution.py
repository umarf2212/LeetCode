class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        onesEnded = False
        for i in range(1, len(s)):
            if s[i] == '0':
                onesEnded = True
            elif onesEnded:
                return False
        
        return True
            