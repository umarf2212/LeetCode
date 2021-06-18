class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        d = {}
        
        symbols = set('!?\',;. ')
        
        i=0
        word = ''
        while i < len(paragraph):
            if paragraph[i] not in symbols:
                word += paragraph[i].lower()
            elif len(word) > 0:
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1
                word = ''
            i+=1
            
        if len(word) > 0:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
                
        for key in banned:
            if key in d:
                del d[key]
        
        mx = float('-inf')
        res = ''
        for key, count in d.items():
            if count > mx:
                mx = count
                res = key
        
        return res