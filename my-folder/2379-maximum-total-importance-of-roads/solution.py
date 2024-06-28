from collections import defaultdict
import heapq
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        # {
        #     2: [1,3,4,0], 5
        #     1: [0,2,3], 4
        #     0: [1,2], 3
        #     3: [1,2], 2
        #     4: [2] 1
        # }

        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        

        pq = []
        for edges in graph.values():
            heapq.heappush(pq, -len(edges))

        result = 0
        while n > 0:
            if not pq:
                break
                
            edges = heapq.heappop(pq) * -1
            result += edges * n

            n -= 1
        
        return result
