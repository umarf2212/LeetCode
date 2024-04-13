from collections import defaultdict
class DetectSquares:

    # We have a point x1, y1
    # Let's consider another point x3, y3 
    # which is on diagonal of the square.
    # The other two points are: x2, y2 = x1, y3 and 
    #                           x4, y4 = x3, y1

    # To check for a square,
    # abs(y3-y1) == abs(x3-x1) and abs(x3-x1) > 0

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[x, y] += 1

    def count(self, point: List[int]) -> int:
        totalCount = 0
        ans = 0

        x1, y1 = point

        for curPoint, count in self.points.items():
            x3, y3 = curPoint

            # x2, y2 = x1, y3
            # x4, y4 = x3, y1

            # is square?
            if abs(y3-y1) == abs(x3-x1) and abs(x3-x1) > 0:
                # check other two points
                if (x1, y3) in self.points and (x3, y1) in self.points:
                    ans += count * self.points[x1, y3] * self.points[x3, y1]
        
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
