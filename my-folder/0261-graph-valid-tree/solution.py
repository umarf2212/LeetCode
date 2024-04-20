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
            return True
        
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        
        elif self.rank[y] > self.rank[x]:
            self.parent[x] = y
        
        else:
            self.parent[y] = x
            self.rank[x] += 1
        
        return False


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. Only 1 CC
        # 2. No simple cycles

        dsu = DSU(n)

        for u, v in edges:
            if dsu.union(u, v):
                return False
        
        CC = 0
        for i in range(len(dsu.parent)):
            if dsu.parent[i] == i:
                CC += 1
        
        return CC == 1

