class Solution:
    def reverseVowels(self, s: str) -> str:

        ar = []
        vowels = 'aeiouAEIOU'
        for i in s:
            if i in vowels:
                ar.append(i)
        
        v = len(ar)-1
        res = ''
        for i in s:
            if i in vowels:
                res += ar[v]
                v-=1
            else:
                res += i
        
        return res
