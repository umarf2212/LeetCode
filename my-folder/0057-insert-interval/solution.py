class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # [1, 2], [3, 6], [9, 10]
        # [4, 8]

        # p---q  a-----b  c----d e----------f  g----h
        #           x---------------------y



        #       --  ------  -----
        #    -----------------------

        #     ----------
        #  --------

        #  -----
        #           -----
    
        # 1. Create result container newIntervals that contains the result
        # 2. Add all starting intervals that do not overlap with newInterval
        # 3. Once one interval overlaps with newInterval, we'll merge these two and     
        #    push them in the newIntervals array.
        # 4. Now, we simply merge the top of newIntervals with every subsequent 
        #    interval, if they both overlap

        n = len(intervals)
        finalIntervals = []

        # Add starting non-overlapping intervals
        i=0
        while i < n and intervals[i][1] < newInterval[0]:
            i+=1
        
        finalIntervals += intervals[:i]
        
        # i is possibly at an overlapping interval
        while i < n and intervals[i][0] <= newInterval[1]:
            curStart, curEnd = intervals[i]
            newInterval[0] = min(newInterval[0], curStart)
            newInterval[1] = max(newInterval[1], curEnd)
            i+=1
        
        finalIntervals.append(newInterval)

        finalIntervals += intervals[i:]

        return finalIntervals




            
        




