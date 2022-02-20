class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        res = []
        i=0
        while i < len(s):
            curr = ''
            for _ in range(k):
                if i == len(s): break
                curr += s[i]
                i += 1
            
            res.append(curr)
        
        last = len(res[-1])
        if last < k:
            res[-1] += (k-last) * fill
        
        return res