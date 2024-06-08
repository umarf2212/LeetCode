class Solution:
    def clearDigits(self, s: str) -> str:
        # arr = [ch for ch in s]
        
        stack = []
        for ch in s:
            if ch.isalpha():
                stack.append(ch)
            elif stack:
                stack.pop()
        
        return ''.join(stack)
            
            
