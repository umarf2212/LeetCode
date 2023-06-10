class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        
        # 1 2 2 4 5 6 3 3 8 9 10
        
        # 1 1 1 1 1 1
        
        i = 0
        j = 0
        repeats = 0
        ans = float('-inf')
        while j < len(s):
            
            if j>0 and s[j-1] == s[j]:
                repeats += 1
            
            if repeats > 1:
                while i < j and s[i] != s[i+1]:
                    i+=1
                
                if s[i] == s[i+1]:
                    repeats -= 1
                    i+=1
            
            ans = max(ans, j-i+1)
            j+=1
        
        return ans
            
                
                
        
