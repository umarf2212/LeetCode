class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        intervals = {}
        for i in range(len(s)):
            if s[i] not in intervals:
                intervals[s[i]] = [i,i]
            else:
                intervals[s[i]][1] = i
        

        intervals = list(intervals.values())
        intervals.sort(key = lambda x:x[0])
        mergedIntervals = [intervals[0]]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            prev = mergedIntervals[-1]

            # prev->last | cur->first
            if prev[1] > cur[0]:
                mergedIntervals.pop()
                new = [ prev[0], max(prev[1], cur[1]) ]
                mergedIntervals.append(new)
            else:
                mergedIntervals.append(cur)

        res = []
        for interval in mergedIntervals:
            res.append(interval[1]-interval[0]+1)
        
        return res



