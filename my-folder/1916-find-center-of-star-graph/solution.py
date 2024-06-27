from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        

        graph = defaultdict(list)
        n = 1
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            n = max(n, u, v)
        
        for i in range(1, n+1):
            if len(graph[i]) == n-1:
                return i
        

        

