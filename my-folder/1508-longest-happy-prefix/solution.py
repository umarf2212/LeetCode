class Solution:
    def longestPrefix(self, s: str) -> str:
        
        n = len(s)

        lps = [0] * n
        for i in range(1, n):
            x = lps[i-1]

            while s[x] != s[i]:
                if x == 0:
                    x = -1
                    break
                x = lps[x-1]
            
            lps[i] = x+1
        
        lpsLen = lps[-1]

        return s[:lpsLen]
