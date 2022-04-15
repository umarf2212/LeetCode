class Solution:
    def countHomogenous(self, s: str) -> int:
        
        getCount = lambda x: (x*(x+1)) // 2
        
        i = 0
        count = 0
        while i < len(s):
            
            j = i+1
            while j<len(s) and s[i] == s[j]:
                j+=1
            
            count += getCount(j-i)
            
            i=j
        
        return count % 1000000007