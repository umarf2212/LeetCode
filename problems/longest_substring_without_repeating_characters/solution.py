class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        
        chars = set()
        i = 0
        j = 0
        maxSize = 1
        while j < len(s):

            if s[j] not in chars:
                chars.add(s[j])
                maxSize = max(maxSize, len(chars))
            else:
                while s[i] != s[j]:
                    chars.remove(s[i])
                    i += 1
                i+=1            
            j+=1
        
        return maxSize