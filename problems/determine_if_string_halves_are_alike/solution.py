class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        # vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        vowels = 'aeiouAEIOU'
        
        n = len(s)
        half = n//2
        x = 0
        for i in range(n):
            if s[i] in vowels:
                if i < half: x+=1
                else: x -= 1
        
        return True if x == 0 else False