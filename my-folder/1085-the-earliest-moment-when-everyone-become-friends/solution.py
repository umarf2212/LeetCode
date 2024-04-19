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

        if x == y: 
            return False
        
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        
        elif self.rank[y] > self.rank[x]:
            self.parent[x] = y
        
        else:
            self.parent[y] = x
            self.rank[x] += 1
        
        return True

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        dsu = DSU(n)

        # logs: [timestamp, x, y]

        logs.sort(key=lambda x:x[0])
        groups = n
        for timestamp, x, y in logs:
            
            if dsu.union(x, y):
                groups -= 1
            
            if groups == 1:
                return timestamp

        return -1

