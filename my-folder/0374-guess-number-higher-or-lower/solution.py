# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        low = 1
        high = n
        mid = (low+high)//2
        
        while guess(mid) != 0:
            mid = (low+high)//2
            
            if guess(mid) < 0:
                high = mid-1
            else:
                low = mid+1
            
        return mid
