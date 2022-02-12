class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        
        # loveleetcode
        # ...010012340 -> first pass LtR
        # 321010012210 -> second pass RtL
        
        res = [float('inf')] * len(s)
        
        dis = -1
        for i in range(len(s)):
            if s[i] == c:
                res[i] = 0
                dis = i
            elif dis >= 0:
                res[i] = abs(i - dis)
        
        dis = -1
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                res[i] = 0
                dis = i
            elif dis >= 0:
                res[i] = min(res[i], abs(i - dis))
        
        return res