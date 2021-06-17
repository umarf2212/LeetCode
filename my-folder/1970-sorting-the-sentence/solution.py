class Solution:
    def sortSentence(self, s: str) -> str:
        
        ar = s.split()
        res = [0]*len(ar)

        for word in ar:
            i = int(word[-1])
            
            res[i-1] = word[:len(word)-1]
            
        return ' '.join(res)
