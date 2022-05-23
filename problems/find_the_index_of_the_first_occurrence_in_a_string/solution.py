class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if len(haystack) < len(needle): return -1
        
        j=0
        i=0
        while i < len(haystack):
            
            temp = i
            if needle[j] == haystack[i]:
                while j < len(needle) and i<len(haystack) and needle[j] == haystack[i]:
                    i+=1
                    j+=1
                
                if j == len(needle):
                    return temp
            
            j=0
            i = temp    
            i+=1
        
        return -1