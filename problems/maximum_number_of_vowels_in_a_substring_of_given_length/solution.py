class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels = set(['a','e','i','o','u'])
        
        vowelCount = 0 # current vowel count
        for i in range(k):
            if s[i] in vowels:
                vowelCount += 1

        ans = vowelCount

        j = k
        while j < len(s):
            i = j-k

            if s[i] in vowels:
                vowelCount -= 1
            
            if s[j] in vowels:
                vowelCount += 1

            ans = max(ans, vowelCount)
            
            j+=1
        
        return ans
            