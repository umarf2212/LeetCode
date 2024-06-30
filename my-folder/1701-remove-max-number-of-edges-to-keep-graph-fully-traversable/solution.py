class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [1 for _ in range(n+1)]
        self.components = n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        x = self.find(u)
        y = self.find(v)

        if x == y:
            return True
        
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        
        elif self.rank[y] > self.rank[x]:
            self.parent[x] = y
        
        elif self.rank[x] == self.rank[y]:
            self.parent[x] = y
            self.rank[y] += 1
        
        self.components -= 1
        
        return False


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        # Consider graph for both Alice and Bob individually 
        # For either of them, the graph must have n-1 edges
        # Use DSU to build graph for Alice and Bob separately
        # Prioritise Type 3 edge, if there are > 1 edges for two nodes,
        # remove the non-type 3 one and increment count

        removed = 0
        removed_type3 = 0

        alice_dsu = DSU(n)
        for type, u, v in edges:
            if type == 3:
                if alice_dsu.union(u, v):
                    removed_type3 += 1
        
        for type, u, v in edges:
            if type == 1:
                if alice_dsu.union(u, v):
                    removed += 1

        bob_dsu = DSU(n)
        for type, u, v in edges:
            if type == 3:
                bob_dsu.union(u, v)
        
        for type, u, v in edges:
            if type == 2:
                if bob_dsu.union(u, v):
                    removed += 1
        
        if alice_dsu.components != 1 or bob_dsu.components != 1:
            return -1
        
        return removed + removed_type3
