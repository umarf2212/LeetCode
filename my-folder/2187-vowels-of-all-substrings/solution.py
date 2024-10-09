class Solution:
    def countVowels(self, word: str) -> int:

        vowels = set(['a','e','i','o','u'])
        n = len(word)
        ans = 0
        for i in range(n):
            letter = word[i]

            if letter in vowels:
                ans += (i+1) * (n-i)
        
        return ans


        # b a c
        # 1 * 1 + 1 = 1

        # b c a d r

        
        # 0 1 2 3 4 5
        # b c a d e f
        #     i

        # (i+1) * (n-i)
        
        
        # 2 * 3 = 6 + 1
        # 4 * 1 = 4 + 1

        # i, j -> 0,0

        # (i, j+1) + (i+1, j)






