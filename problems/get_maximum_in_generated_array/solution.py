class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n==0: return 0
        
        ar = [0] * (n+1)
        ar[0] = 0
        ar[1] = 1
        
        i=1
        while 2*i+1 <= n:
            ar[2 * i] = ar[i]
            ar[2 * i + 1] = ar[i] + ar[i+1]
            i+=1
        
        return max(ar)