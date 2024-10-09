class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []
        minMoves = 0

        for p in s:
            if p == '(':
                stack.append('(')
            
            elif not stack:
                minMoves += 1
                
            else:
                stack.pop()
        
        return minMoves + len(stack)


