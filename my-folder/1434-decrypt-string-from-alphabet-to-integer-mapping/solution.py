class Solution:
    def freqAlphabets(self, s: str) -> str:
        
        p1 = ['a','b','c','d','e','f','g','h','i']
        p2 = ['j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        res = ''
        i = 0
        while i < len(s)-2:
            
            if s[i+2] == '#':
                res += p2[int(s[i]+s[i+1]) - 10]
                i+=3
            else:
                res += p1[int(s[i])-1]
                i+=1
        
        if s[-1] != '#':
            if s[-2] != '#': res += p1[int(s[-2])-1]
            res += p1[int(s[-1])-1]

        
        return res
