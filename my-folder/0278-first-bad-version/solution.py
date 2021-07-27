# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        low = 0
        high = n
        res = 0
        
        while low <= high:
            
            mid = (low+high)//2
            
            if isBadVersion(mid+1):
                res = mid+1
                high = mid-1
            else:
                low = mid+1
        
        return res
