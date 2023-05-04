class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShipPackages(weights, days, maxWeight):
            daysCount = 1
            curWeight = 0
            for i in range(len(weights)):
                curWeight += weights[i]
                if curWeight > maxWeight:
                    curWeight = weights[i]
                    daysCount += 1
                
            if daysCount > days:
                return False
            return True 

        lo = max(weights)
        hi = sum(weights)
        while lo <= hi:
            mid = (lo+hi)//2

            if canShipPackages(weights, days, mid):
                hi = mid-1
            else:
                lo = mid+1
        
        return lo