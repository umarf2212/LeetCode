class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for b in s:

            if b in '([{':
                stack.append(b)
            
            elif b == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            
            elif b == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            
            elif b == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False
