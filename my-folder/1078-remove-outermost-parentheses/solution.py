class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        res = ''
        stack = []
        openingCount = 0
        
        for p in s:
            if p == '(':
                if openingCount > 0:
                    res += p
                    openingCount += 1
                else:
                    openingCount = 1
                
            elif p == ')':
                if openingCount > 1:
                    res += p
                    openingCount -= 1
                else:
                    openingCount = 0
        
        return res
                
