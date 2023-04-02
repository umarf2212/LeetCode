class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        
        # Find first occurrence of positive
        # Find last occurrence of negative

        n = len(nums)

        # First occurrence of positive
        lo = 0
        hi = len(nums)-1
        firstPos = -1
        while lo <= hi:
            mid = (lo+hi)//2

            if nums[mid] <= 0:
                lo = mid + 1
            else:
                firstPos = mid
                hi = mid - 1
        
        # Last occurrence of negative
        lo = 0
        hi = len(nums)-1
        lastNeg = -1
        while lo <= hi:
            mid = (lo+hi)//2

            if nums[mid] < 0:
                lastNeg = mid
                lo = mid + 1
            else:
                hi = mid - 1

        if firstPos == -1 and lastNeg == -1:
            return 0
        elif firstPos == -1:
            return lastNeg + 1
        elif lastNeg == -1:
            return n-firstPos

        return max( lastNeg + 1, n - firstPos )

