class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        big = start if start > goal else goal
        small = start if start < goal else goal
        
        big = bin(big)[2:]
        small = bin(small)[2:]
        
        count = 0
        m = len(small)
        n = len(big)
        for i in range(m):
            count += int(small[m-i-1]) ^ int(big[n-i-1])
        
        i+=1
        while n-i-1 >= 0:
            if big[n-i-1] == '1':
                count += 1
            i+=1
        
        
        return count