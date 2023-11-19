class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        deg = [0] * (n+1)

        # adj = defaultdict(list)
        # for edge in trust:
        #     u = edge[0]
        #     v = edge[1]
        #     adj[u] = v

        for edge in trust:
            u = edge[0]
            v = edge[1]

            deg[u] -= 1
            deg[v] += 1
        
        for i in range(1, n+1):
            if deg[i] == n-1:
                return i
        
        return -1
        
