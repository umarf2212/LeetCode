from collections import defaultdict
import heapq
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.distCache = {}

        self.adj = defaultdict(list)
        self.wt = {}
        for i, j, w in edges:
            self.adj[i].append(j)
            self.wt[i, j] = w

    def addEdge(self, edge: List[int]) -> None:
        i, j, w = edge
        self.adj[i].append(j)
        self.wt[i, j] = w

    def shortestPath(self, node1: int, node2: int) -> int:
        if (node1, node2) in self.distCache:
            return self.distCache[node1, node2]
        
        dist = self.dijkstra(node1)

        if dist[node2] == float('inf'):
            return -1

        return dist[node2]
    
    def dijkstra(self, S):
        d = [float('inf')] * self.n
        heap = [(0, S)]
        
        while heap:
            dist, v = heapq.heappop(heap)
            
            if d[v] == float('inf'):
                d[v] = dist
            
                for u in self.adj[v]:
                    if d[u] == float('inf'):
                        heapq.heappush(heap, (dist + self.wt[v, u], u))
        
        self.distCache[S] = d
        return d



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
