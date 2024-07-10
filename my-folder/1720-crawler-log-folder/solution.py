class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        folder = 0

        for log in logs:
            if log == '../':
                folder = max(0, folder-1)
            
            elif log != './':
                folder += 1

        return folder
