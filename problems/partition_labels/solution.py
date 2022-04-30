class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        intervals = {}
        seen = set()
        for i in range(len(s)):
            if s[i] not in intervals:
                j = len(s)-1
                while s[j] != s[i]:
                    j-=1
                
                intervals[s[i]] = [i,j]
        
        intervals = list(intervals.values())
        intervals.sort(key=lambda x: x[0])
        
        # print(intervals)
        
        mergedIntervals = []
        i=0
        while i < len(intervals)-1:
            start = intervals[i][0]
            currEnd = intervals[i][1]
            # if intervals overlap
            if intervals[i][1] >= intervals[i+1][0]:
                currEnd = intervals[i][1]
                while i<len(intervals)-1 and currEnd >= intervals[i+1][0]:
                    currEnd = max(currEnd, intervals[i+1][1])
                    i+=1
            
            mergedIntervals.append(currEnd-start+1)
            i += 1
        
        if i < len(intervals):
            mergedIntervals.append(intervals[i][1]-intervals[i][0]+1)
            
        return mergedIntervals