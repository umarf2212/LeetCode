class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        res = []
        i=0
        while i < len(intervals)-1:
            
            
            if intervals[i][1] >= intervals[i+1][0]:
                start = intervals[i][0]
                
                currEnd = intervals[i][1]
                while i < len(intervals)-1 and currEnd >= intervals[i+1][0]:
                    currEnd = max(currEnd, intervals[i+1][1])
                    i+=1
                
                res.append([start, currEnd])
            
            else:
                res.append(intervals[i])
            
            i+=1
        
        if i == len(intervals)-1:
            res.append(intervals[i])
            
        return res