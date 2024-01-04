class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x:x[1])

        count = 0
        end = intervals[0][1]
        for i in range(1, len(intervals)):

            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]
        
        return count


        #  [ [1,2] [1,3] [2,3] [3,4] ]


        #  [ [1,2] [1,3] [3,4] [4,5] ]


        #  [ [1,2] [1,4] [2,3] [3,4] ]




