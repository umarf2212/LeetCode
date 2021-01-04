class Solution:
    def reverseVowels(self, s: str) -> str:
        
        left = 0
        right = len(s)-1
        
        vowels = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1, 'A':1,'E':1,'I':1,'O':1,'U':1}

        strAr = [i for i in s]
        
        while left < right:
            if strAr[left] not in vowels: left += 1
            
            if strAr[right] not in vowels: right -= 1
                
            if strAr[left] in vowels and strAr[right] in vowels:
                strAr[left], strAr[right] = strAr[right], strAr[left]               
                left += 1
                right -= 1
                
        return ''.join(strAr)
