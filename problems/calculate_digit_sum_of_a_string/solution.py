class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            ar = []
            for i in range(0, len(s), k):
                ar.append(s[i:i+k])

            res = ''
            for part in ar:
                res += str(sum([int(i) for i in part]))
            
            s = res
        
        return s