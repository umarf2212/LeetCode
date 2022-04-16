class Solution:
    def numSub(self, s: str) -> int:
        
        getCount = lambda x: (x*(x+1)) // 2
        
        count = 0
        i = 0
        while i < len(s):
            if s[i] == '1':
                j = i+1
                while j < len(s) and s[j] == '1':
                    j+=1
            
                count += getCount(j-i)
            
                i = j
            else:
                i += 1
            
        
        return count % 1000000007
            
