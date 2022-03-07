class Solution:
    def minPartitions(self, n: str) -> int:
        mx = float('-inf')
        for i in range(len(n)):
            i = int(n[i])
            if i > mx:
                mx = i
        
        return mx