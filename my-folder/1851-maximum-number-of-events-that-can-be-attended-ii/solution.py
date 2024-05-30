class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        events.sort(key=lambda x:x[0])
        
        def findNextEventInd(ind, events):
            curEnd = events[ind][1]
            nextEventInd = len(events)

            left = ind+1
            right = len(events)-1
            while left <= right:
                mid = (left+right)//2
                nextStart = events[mid][0]

                if nextStart > curEnd:
                    nextEventInd = mid
                    right = mid-1
                else:
                    left = mid+1
            
            return nextEventInd

        def maxEventValue(ind, k, dp):
            if k == 0 or ind >= len(events):
                return 0
            
            if dp[ind][k] != -1:
                print(ind, k)
                return dp[ind][k]

            nextEventInd = findNextEventInd(ind, events)

            curRes = max( maxEventValue(ind+1, k, dp), events[ind][2] + maxEventValue(nextEventInd, k-1, dp) )
            dp[ind][k] = curRes

            return curRes
        

        dp = [[-1 for _ in range(k+1)] for _ in range(len(events))]
        print(dp)
        return maxEventValue(0, k, dp)

        # 1. Sort the events by start time
        # 2. At any event i, you either choose that event or skip it.
        # 3. If you do not choose i, move on to i+1
        # 4. If you do choose i, you search for the startDay greater than endDay of the current event.
        # 5. Terminate recursion if k == 0

        # State Representation: the index i of events, k
        # State transition: 
            # (i+1) or (next i = events[i][1] <  events[nextEventInd][0])
            # k = k-1 for a choice

        # memo: i, k => on a given day for every k, what was the max value

        # Final result: k == 0 and i == len(events)-1

        # Base Cases: 
            # k == 0: return 0
            # i >= len(events) => return 0

        # Recurrence Relation: 
            # maxEventValue(i, k) =  max( maxEventValue(i+1, k), events[i][2] + maxEventValue(nextEventInd, k-1) )

        # Find nextEventInd:
        # Since the events array is sorted by startTime, and we have to find startTime only, 
        # we can perform Binary Search to find the next event that has lowest startTime > curEndTime

