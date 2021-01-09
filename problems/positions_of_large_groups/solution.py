class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        
        intervals = []
        start = 0
        s+='0'
        
        for i in range(1,len(s)):
            
            if s[i] != s[i-1]:
                
                if i-1 - start >= 2:
                    intervals.append([start, i-1])
                    
                start = i
                
        
        return intervals