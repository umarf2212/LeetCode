class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        ar = [1]
        for i in range(2, int(n**0.5)+1):
            if not n % i:
                ar.append(i)
            
                if n // i != i:
                    ar.append(n // i)
        
        ar.sort()
        ar.append(n)
        if k > len(ar):
            return -1
        return ar[k-1]