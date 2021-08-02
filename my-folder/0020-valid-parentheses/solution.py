class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        opening = '([{'
        closing = {')': '(', ']': '[', '}': '{'}
        
        for b in s:
            
            if b in opening:
                stack.append(b)
            
            elif len(stack)==0 or stack[-1] != closing[b]:
                return False
            
            elif stack[-1] == closing[b]:
                stack.pop()
            
        return len(stack) == 0
