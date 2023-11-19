class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        for edge in edges:
            u = edge[0]
            v = edge[1]

            adj[u].append(v)
            adj[v].append(u)
        
        n = len(adj.keys())
        
        for v, deg in adj.items():

            if len(deg) == n-1:
                return v