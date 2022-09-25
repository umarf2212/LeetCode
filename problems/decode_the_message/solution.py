class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        d = {}
        for i in key:
            if i not in d and i != ' ':
                d[i] = 0
        
        
        table = {' ':' '}
        i = 0
        k = list(d.keys())
        for ch in sorted(k):
            table[k[i]] = ch
            i+=1
        
        res = ''
        for ch in message:
            res += table[ch]
        
        return res
        
        
            
            