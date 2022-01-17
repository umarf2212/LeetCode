class Solution:
    def maxDepth(self, s: str) -> int:
        
        max_depth = 0
        
        curr_depth = 0
        
        for i in range(len(s)):
            
            if s[i] == '(':
                curr_depth += 1
                if curr_depth > max_depth:
                    max_depth = curr_depth
            
            elif s[i] == ')':
                curr_depth -= 1
            
        return max_depth
