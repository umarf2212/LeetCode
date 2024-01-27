class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # [1,2] [1,3] [2,3] [3,4]

        # Sorting intervals by end in ASC means
        # former intervals are as farther to the left
        # as possible. Hence any latter intervals that 
        # overlap them means there's no other way but to 
        # remove them.

        intervals.sort(key = lambda x:x[1])

        _, end = intervals[0]
        count = 0
        for i in range(1, len(intervals)):
            curStart, curEnd = intervals[i]

            # overlapping, this has to be removed
            if curStart < end:
                count += 1
            
            # not overlapping, move on, update cur start and end
            else:
                end = curEnd
        
        return count






