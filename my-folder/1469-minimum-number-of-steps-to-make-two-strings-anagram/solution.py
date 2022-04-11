class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        S = Counter(s)
        T = Counter(t)
        
        res = 0
        for letter, count in S.items():
            if letter not in T:
                res += count
            else:
                if T[letter] < count:
                    res += count - T[letter]
        
        return res
