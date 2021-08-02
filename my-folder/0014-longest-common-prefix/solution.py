class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ln = 0
        
        smallest_len = float('inf')
        for word in strs:
            smallest_len = min(smallest_len, len(word))
        
        if smallest_len == 0: return ""
        
        i = 0
        while i < smallest_len:
            
            for word in strs:
                if word[i] != strs[0][i]:
                    return strs[0][:i]
            
            i+=1
        
        return strs[0][:i]
