from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, v):
        if self.parent[v] == v:
            return v
        
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, u, v):
        x = self.find(u)
        y = self.find(v)

        if x == y:
            return False
        
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.rank[x] += self.rank[y]
        
        elif self.rank[y] > self.rank[x]:
            self.parent[x] = y
            self.rank[y] += self.rank[x]

        else:
            self.parent[y] = x
            self.rank[x] += self.rank[y]
    
    def getSize(self, x):
        return self.rank[self.find(x)]
        

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        

        # graph = defaultdict(list)
        connected = 0
        restrictedSet = set(restricted)
        dsu = DSU(n)
        for u, v in edges:
            if u in restrictedSet or v in restrictedSet:
                continue
            
            dsu.union(u, v)

        return dsu.getSize(0)
        
        # def dfs(node, ans):
        #     vis.add(node)

        #     ans[0] += 1

        #     for neighbor in graph[node]:
        #         if neighbor not in vis:
        #             dfs(neighbor, ans)


        # vis = set(restricted)
        # ans = [0]
        # dfs(0, ans)
        # return ans[0]
