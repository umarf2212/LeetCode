class Solution:
    def compressedString(self, word: str) -> str:

        # aaabcd
        # aaabdd
        
        comp = ''
        curChar = word[0]
        count = 1
        for i in range(len(word)-1):
            if word[i] == word[i+1] and count < 9:
                count += 1
            else:
                comp += str(count) + curChar
                curChar = word[i+1]
                count = 1

        comp += str(count) + curChar

        return comp


