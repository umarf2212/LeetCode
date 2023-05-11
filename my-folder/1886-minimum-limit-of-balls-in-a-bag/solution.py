import heapq
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def canBallsBeOperated(nums, ballsPerOperation, maxOperations):
            '''balls = balls per operation'''

            operations = 0
            for balls in nums:
                if balls >= ballsPerOperation:
                    operations += (balls-1) // ballsPerOperation
            
            if operations > maxOperations:
                return False
            return True

        lo = 1
        hi = max(nums)
        while lo <= hi:
            mid = (lo+hi)//2

            if canBallsBeOperated(nums, mid, maxOperations):
                hi = mid - 1
            else:
                lo = mid + 1
        
        return lo
