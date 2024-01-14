from functools import cmp_to_key
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = lambda x, y: sqrt(x**2 + y**2)
        
        def compare(a, b):
            return dist(a[0], a[1]) - dist(b[0], b[1])


        return sorted(points, key=cmp_to_key(compare))[:k]


