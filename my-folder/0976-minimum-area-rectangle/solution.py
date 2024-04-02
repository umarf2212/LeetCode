class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        # points.sort(key=lambda x:x[0])
        
        n = len(points)
        pointsSet = set([tuple(point) for point in points])

        def checkRectangle(x1, y1, x2, y2):
            return x1 < x2 and y1 < y2 and (x1, y2) in pointsSet and (x2, y1) in pointsSet

        ans = float('inf')
        for i in range(n):
            for j in range(n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if checkRectangle(x1, y1, x2, y2):
                    area = (x2 - x1) * (y2 - y1)
                    ans = min(ans, area)
        
        return ans if ans != float('inf') else 0

