class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        
        mx = len(s)
        mn = 0
        
        res = []
        
        for i in s:
            if i == 'I':
                res.append(mn)
                mn += 1
            else:
                res.append(mx)
                mx -= 1
        
        if mn <= len(s):
            res.append(mn)
        elif mx >= 0:
            res.append(mx)
        
        return res
