class Solution:
    def minTimeToType(self, word: str) -> int:
        
        # alpha = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
        
        def alpha(char):
            a = 'abcdefghijklmnopqrstuvwxyz'
            for i in range(26):
                if a[i] == char:
                    return i
        
        res = abs(alpha('a') - alpha(word[0]))
        res = min(26-res, res)
        for i in range(1,len(word)):
            pos = abs(alpha(word[i]) - alpha(word[i-1]))
            res += min(pos, 26 - pos) + 1
        
        return res+1