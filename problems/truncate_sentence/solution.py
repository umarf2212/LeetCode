class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # return ' '.join(s.split()[:k])
        
        c = 0
        new = ''
        i = 0
        while i < len(s):
            
            if s[i] == ' ': c+=1
            
            if c == k: break
                
            new += s[i]
            
            i+=1
            
        return new