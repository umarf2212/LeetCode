from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        wt = {}
        for i in range(len(edges)):
            u, v = edges[i]
            graph[u].append(v)
            graph[v].append(u)
            wt[u,v] = succProb[i]
            wt[v,u] = succProb[i]
        
        # 0 indicates that we haven't yet found a path yet to any of the nodes, and
        # nodes are unreachable unless proven otherwise (updated at some stage)
        distance = [0] * n

        # since we want a max heap (longest path in a graph using Dijsktra),
        # we always store negative values in the heap
        heap = [(-1, start_node)]
        while heap:
            curDist, node = heapq.heappop(heap)

            # change the sign back to positive
            curDist = -curDist

            if distance[node] > curDist:
                continue

            distance[node] = curDist

            for u in graph[node]:
                # probability of a series of events multiple, not add up!
                newDist = curDist * wt[node, u]

                if newDist > distance[u]:
                    heapq.heappush( heap, (-newDist, u) )

        # print(distance)
        return distance[end_node]
