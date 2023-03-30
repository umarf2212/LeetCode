class Solution:
    '''
    Also, check notes for this problem.
    '''
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def canTotalTripsBeDone(targetTime):
            trips = 0
            for t in time:
                # the individual contribution of each bus
                # within this target time
                trips += targetTime // t
            
            return trips >= totalTrips

        lo = 1
        hi = max(time) * totalTrips
        ans = -1
        while lo <= hi:
            mid = (lo+hi) // 2

            if canTotalTripsBeDone(mid):
                hi = mid - 1
                ans = mid
            else:
                lo = mid + 1
        
        return ans


