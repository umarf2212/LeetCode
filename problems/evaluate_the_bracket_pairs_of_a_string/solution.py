class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        
        d = {ar[0]:ar[1] for ar in knowledge}
        
        res = ''
        isKey = False
        key = ''
        for i in range(len(s)):
            if s[i] == ')':
                if key in d:
                    res += d[key]
                else:
                    res += '?'
                    
                key =''
                isKey = False
            
            elif s[i] == '(':
                isKey = True
                
            elif isKey:
                key += s[i]
            
            elif not isKey:
                res += s[i]
        
        return res