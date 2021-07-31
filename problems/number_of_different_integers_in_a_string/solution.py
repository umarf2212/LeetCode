class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        
        ans = set()
        
        start = -1        
        for i in range(len(word)):
            
            if word[i].isdigit() and start == -1:
                start = i
            
            elif word[i].isalpha() and start >= 0:
                ans.add(int(word[start:i]))
                start =- 1
                
        if start >= 0:
            ans.add(int(word[start:i+1]))
        
        return len(ans)