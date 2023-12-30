from functools import cache
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        # We obviously need to figure out if points are collinear 
        # by calculating their slopes.

        # This means we will need to consider each and every possible 
        # pair of points to check their slope. So this problem with this 
        # approach can't be solved in better TC than O(N^2)

        @cache
        def GCD(a, b):
            if b == 0:
                return a
            return GCD(b, a%b)

        n = len(points)
        ans = 1
        d = {}
        for i in range(n):
            overlaps = 0
            curMax = float('-inf')
            for j in range(i+1, n):

                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 == x2 and y1 == y2:
                    overlaps += 1

                x = x2 - x1
                y = y2 - y1

                gcd = GCD(x, y)

                x = x // gcd
                y = y // gcd

                slope = (x, y)

                d[slope] = d.get(slope, 0) + 1
                
                curMax = max(curMax, d[slope])
            
            d = {}
            ans = max(ans, curMax+overlaps+1)
        
        return ans


