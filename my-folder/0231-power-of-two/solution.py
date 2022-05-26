class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        
        setBit = 0
        for _ in range(32):
            
            if setBit > 1:
                return False
            
            if n & 1 == 1:
                setBit += 1
            
            n >>= 1
            
        return True
