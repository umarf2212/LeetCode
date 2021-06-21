class Solution:
    def maxPower(self, s: str) -> int:
        
        prev = s[0]
        maxCount = 1
        currCount = 1
        for i in range(1,len(s)):
            
            if s[i] == prev:
                currCount += 1
                if currCount > maxCount: maxCount = currCount
            else:
                currCount = 1
            
            prev = s[i]
        
        return maxCount
