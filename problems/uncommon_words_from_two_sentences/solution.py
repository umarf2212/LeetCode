class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d = Counter(s1.split())
        
        for word in s2.split():
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
        
        res = []
        for key, val in d.items():
            if val == 1:
                res.append(key)
                
                
        return res