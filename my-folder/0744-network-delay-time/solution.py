from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # 1. Build Graph
        # 2. Use Dijkstra's algo to find shortest path from 
        #    given node to all other nodes.
        # 3. Minimum time to reach all nodes is the time 
        #    it takes for the furthest node to receive the signal.
        # 4. Graph can be disconnected in which case disconnected nodes
        #    may never receive the signal, so return -1 if such node exists.
        

        graph = defaultdict(list)
        wt = {}
        for u, v, w in times:
            graph[u].append(v)
            wt[u, v] = w
        
        inf = float('inf')

        heap = [(0, k)]
        distances = [inf] * (n+1)
        distances[k] = 0
        while heap:
            curDist, v = heappop(heap)

            for u in graph[v]:
                newDist = distances[v] + wt[v, u]

                if newDist < distances[u]:
                    distances[u] = newDist
                    heappush(heap, (newDist, u) )

        maxDist = 0
        for i in range(1, n+1):
            if distances[i] == inf:
                return -1
            else:
                maxDist = max(maxDist, distances[i])
        
        return maxDist



