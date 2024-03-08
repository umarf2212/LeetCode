class Solution:
    def shortestPalindrome(self, s: str) -> str:

        # Direct implementaion of KMP Algorithm
        
        S = s + '@' + s[::-1]

        n = len(S)

        lps = [0] * n
        for i in range(1, n):
            x = lps[i-1]

            while S[x] != S[i]:
                if x == 0:
                    x = -1
                    break
                x = lps[x-1]
            
            lps[i] = x+1
        
        lpsLen = len(s) - lps[-1]

        # print(lps)
        # print(lpsLen)

        if lpsLen > 0:
            return s[-lpsLen:][::-1] + s

        return s
