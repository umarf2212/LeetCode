class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        opening = '([{'
        pairs = {']':'[', '}':'{', ')':'('}
        
        for i in s:
            
            if i in opening:
                stack.append(i)
                
            elif not stack or stack[-1] != pairs[i]:
                return False
            
            elif stack and stack[-1] == pairs[i]:
                stack.pop()
        
        return len(stack) == 0