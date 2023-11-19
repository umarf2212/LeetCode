class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adj = defaultdict(list)
        for edge in edges:
            u = edge[0]
            v = edge[1]

            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(v):
            visited.add(v)

            if v == destination:
                return True

            for u in adj[v]:
                if u not in visited:
                    if dfs(u):
                        return True
        
        return dfs(source)