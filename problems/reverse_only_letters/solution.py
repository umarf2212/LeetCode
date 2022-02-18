class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        newS = ''
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                newS += s[i]
        
        i=0
        j=0
        res=''
        for i in range(len(s)):
            if s[i].isalpha():
                res += newS[j]
                j+=1
            else:
                res += s[i]            
        
        return res