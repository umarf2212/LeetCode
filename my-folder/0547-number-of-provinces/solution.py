class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    def find(self, v):
        if self.parent[v] == v:
            return v
        
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self, u, v):
        x = self.find(u)
        y = self.find(v)

        if x == y: return

        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        
        elif self.rank[y] > self.rank[x]:
            self.parent[x] = y
        
        else:
            self.parent[y] = x
            self.rank[x] += 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)

        dsu = DSU(n)

        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j] == 1:
                    # i <---edge---> j
                    dsu.union(i, j)
        
        CC = 0
        for i in range(n):
            if i == dsu.parent[i]:
                CC += 1
            
        return CC

