from heapq import heappop, heappush
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # DIJKSTRA
        graph = defaultdict(list)
        wt = {}
        for v, u, w in flights:
            graph[v].append(u)
            wt[v, u] = w

        # (distanceFromSrc, src, curStopsCount)
        inf = float('inf')
        distances = [inf] * n
        stops = [inf] * n

        distances[src] = 0
        stops[src] = 0

        heap = [(0, src, 0)]
        while heap:
            curDist, curNode, curStops = heappop(heap)

            # If we have reached destination, return the cost it took.
            # We either reached this through cheapest path possible,
            # or a more expensive path but within K stops constraint.
            if curNode == dst:
                return curDist
            
            # Don't explore further, max limit of k reached.
            # >k because curNode could be the (K+1)th stop 
            # and limit of K stops is before the last node.
            if curStops > k:
                continue

            for nextNode in graph[curNode]:
                newDist = curDist + wt[curNode, nextNode]
                newStops = curStops + 1

                if newDist < distances[nextNode] or newStops < stops[nextNode]:
                    distances[nextNode] = newDist
                    stops[nextNode] = newStops
                    heappush(heap, (newDist, nextNode, newStops) )

        return -1
