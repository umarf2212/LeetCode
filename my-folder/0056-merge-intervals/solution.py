class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        
        res = []
        for i in range(len(intervals)):
            
            if res and intervals[i][0] <= res[-1][1]:
                prev = res.pop()
                start = prev[0]
                end = max(prev[1], intervals[i][1])
                res.append([start, end])
            else:
                res.append(intervals[i])
            
        return res
