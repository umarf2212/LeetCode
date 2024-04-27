class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        if len(s) == 0: return 0

        # xx.xaebcd.eef
        
        S = set()
        i = 0
        j = 0
        n = len(s)
        maxLen = 1
        while j < n:

            if s[j] not in S:
                S.add(s[j])
                maxLen = max(maxLen, len(S))
            
            else:
                while s[i] != s[j]:
                    S.remove(s[i])
                    i += 1

                i+=1
            
            j+=1
        
        return maxLen
                



