class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        # RLRRLLRLRL
        
        stack = []
        count = 0
        for i in s:
            if not stack or i == stack[-1]:
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    count+=1
        
        return count
