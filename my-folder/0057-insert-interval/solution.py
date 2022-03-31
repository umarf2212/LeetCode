class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals: return [newInterval]
        
        if newInterval[1] < intervals[0][0]:
            return [newInterval, *intervals]
        
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        
        res = []
        i=0
        while i < len(intervals):
            curr = intervals[i]
            
            if curr[0] <= newInterval[1] and newInterval[0] <= curr[1]:
                
                left = min(newInterval[0], curr[0])
                
                while i < len(intervals) and newInterval[1] >= intervals[i][0]:
                    i+=1
                    
                right = max(newInterval[1], intervals[i-1][1])
                
                res.append([left, right])
                break
            
            else:
                res.append(intervals[i])
                
                if newInterval[0] > intervals[i][1] and newInterval[1] < intervals[i+1][0]:
                    res.append(newInterval)
            
            i+=1
        
        # if i < len(intervals)-1:
        res += intervals[i:]
                                                                            
        return res
