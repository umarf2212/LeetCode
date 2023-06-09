class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): return False

        p = s1
        s = s2

        P = {}
        for c in p:
            if c not in P:
                P[c] = 0
            P[c] += 1

        def checkSame(cur, d):
            for key, count in cur.items():
                if key not in d:
                    return False
                elif d[key] != count:
                    return False
            return True

        cur = {}
        for i in range(len(p)):
            if s[i] not in cur:
                cur[s[i]] = 0
            cur[s[i]] += 1
        
        res = []
        for j in range(len(p), len(s)):
            i = j-len(p)

            if checkSame(cur, P):
                return True
            
            cur[s[i]] -= 1
            if cur[s[i]] == 0:
                del cur[s[i]]

            if s[j] not in cur:
                cur[s[j]] = 0
            cur[s[j]] += 1
        
        if checkSame(cur, P):
            return True

        return False