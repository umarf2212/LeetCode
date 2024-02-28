from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        adj = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
        
        def dfs(v):
            vis.add(v)
            for u in adj[v]:
                if u not in vis:
                    dfs(u)
        
        res = 0
        vis = set()
        for i in range(n):
            if i not in vis:
                dfs(i)
                res += 1
        
        return res

