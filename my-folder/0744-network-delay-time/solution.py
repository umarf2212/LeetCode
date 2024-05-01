import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        inf = float('inf')

        graph = defaultdict(list)
        wt = {}
        for u,v,w in times:
            graph[u].append(v)
            wt[u, v] = w
        
        distances = [inf] * (n+1)

        hq = []
        heapq.heappush(hq, (0, k))

        while hq:
            dist, v = heapq.heappop(hq)

            if distances[v] == inf:
                distances[v] = dist

                for u in graph[v]:
                    if distances[u] == inf:
                        heapq.heappush(hq, (dist+wt[v, u], u))
        
        # print(distances)

        ans = -1
        for dist in distances[1:]:
            ans = max(ans, dist)
        
        if ans == inf: 
            return -1
        
        return ans
