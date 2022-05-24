class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        '''
        aa aa aa aa aa
        
        bb bb b
        
        aa bb aa b aa b aa
        
        [aa, aa, aa, aa, aa]
        [bb, bb, b]
              i
        '''
        aPairs = divmod(a, 2)
        bPairs = divmod(b, 2)
        
        aPairs = ['aa'] * aPairs[0] + ['a'] * aPairs[1]
        bPairs = ['bb'] * bPairs[0] + ['b'] * bPairs[1]
        
        if len(aPairs) < len(bPairs):
            small = aPairs
            big = bPairs
        else:
            small = bPairs
            big = aPairs
        
        pairPosition = len(small)-1
        while pairPosition > 0 and len(small[pairPosition]) == 1:
            pairPosition -= 1
            
            
        smallCount = len(small)
        smallChar = small[0][0]
        for b in range(len(big)-1):
            if smallCount <= 0:
                small[pairPosition] = smallChar
                small.append(smallChar)
                pairPosition -= 1
            
            smallCount -= 1
        
        i = 0
        j = 0
        res = ''
        while i < len(small) and j < len(big):
            res += big[j] + small[i]
            i+=1
            j+=1
        
        if i < len(big):
            res += big[i]
        
        return res