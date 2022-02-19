class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []
        
        for log in logs:
            
            if log == './':
                continue
            
            elif log == '../':
                if not stack:
                    continue
                else:
                    stack.pop()
            
            else:
                stack.append(log)
        
        
        return len(stack)
