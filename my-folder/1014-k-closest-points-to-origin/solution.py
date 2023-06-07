class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        pq = []
        
        for point in points:
            x = point[0]
            y = point[1]
            d = sqrt(x**2 + y**2)
            heapq.heappush(pq, (d, point))
        
        ar = []
        while k > 0:
            ar.append(heapq.heappop(pq)[1])
            k-=1
        
        return ar
