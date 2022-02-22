class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        if len(points) == 1: 
            return 0
        
        ans = 0
        
        for i in range(1, len(points)):
            
            curr = points[i]
            prev = points[i-1]
            ans += max(abs(curr[0]-prev[0]), abs(curr[1]-prev[1]))
        
        return ans