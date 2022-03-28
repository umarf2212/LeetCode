class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        points.sort(key=lambda x: x[0])
        maxDiff = float('-inf')
        
        for i in range(1, len(points)):
            diff = points[i][0] - points[i-1][0]
            
            if diff > maxDiff:
                maxDiff = diff
        
        return maxDiff             
            
            
