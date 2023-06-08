class Solution:
    def sortString(self, s: str) -> str:

        ar = [i for i in s]
        ar.sort()

        d = {}
        for c in ar:
            if c not in d:
                d[c] = 0
            d[c] += 1

        i = 0
        res = ''
        while d:

            keys = list(d.keys()) if i%2 == 0 else list(d.keys())[::-1]

            for ch in keys:
                if d[ch] == 0:
                    del d[ch]
                else:
                    res += ch
                    d[ch] -= 1

            i+=1
        
        return res