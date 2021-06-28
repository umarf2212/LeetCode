class Solution:
    def checkRecord(self, s: str) -> bool:
        
        return not(Counter(s)['A'] > 1 or 'LLL' in s)
                
