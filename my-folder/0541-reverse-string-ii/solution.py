class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        alt = True
        start = 0
        new = ''
        for i in range(0, len(s), k):
            
            if alt:
                new += s[start:start+k][::-1]
                start += k
                alt = False
            else:
                new += s[start:start+k]
                start += k
                alt = True
        
        return new
