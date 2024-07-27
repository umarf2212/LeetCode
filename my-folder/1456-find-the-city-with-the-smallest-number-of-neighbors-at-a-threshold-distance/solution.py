class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        graph = [[float('inf')] * n for _ in range(n)]
        for v, u, wt in edges:
            graph[v][u] = wt
            graph[u][v] = wt

        for i in range(n):
            graph[i][i] = n
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if graph[i][j] > graph[i][k] + graph[k][j]:
                        graph[i][j] = graph[i][k] + graph[k][j]
        
        cities = [0] * n
        for i in range(n):
            for j in range(n):
                if i==j: continue
                
                if graph[i][j] <= distanceThreshold:
                    cities[i] += 1

        minPaths = float('inf')
        ans = -1
        for i in range(n):
            if cities[i] <= minPaths:
                minPaths = cities[i]
                ans = i
        
        return ans

            
