class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        n = len(points)

        pointsSet = set([tuple(point) for point in points])

        def checkRectangle(x1, y1, x2, y2, pointsSet):
            if x2 > x1 and y2 > y1 and (x2, y1) in pointsSet and (x1, y2) in pointsSet:
                return True
            return False

        ans = float('inf')
        for i in range(n):
            for j in range(n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if checkRectangle(x1, y1, x2, y2, pointsSet):
                    area = (x2-x1) * (y2-y1)
                    ans = min(area, ans)

        return ans if ans != float('inf') else 0
