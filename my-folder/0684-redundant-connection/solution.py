class DSU:
    def __init__(self, N):
        self.parent = [i for i in range(N+1)]
        self.rank = [1] * (N+1)
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        '''
        returns True if x and y have same parent
                False if x and y were united
        '''
        X = self.find(x)
        Y = self.find(y)

        if X == Y:
            return True
        
        if self.rank[X] > self.rank[Y]:
            self.parent[Y] = X
        
        elif self.rank[Y] > self.rank[X]:
            self.parent[X] = Y
        
        elif self.rank[X] == self.rank[Y]:
            self.parent[X] = Y
            self.rank[Y] += 1
        
        return False
            


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        # 1. Use DSU to find out the redundant edge in the graph.
        # 2. DSU will help because as per the ordering of the nodes in the input, 
        #    we'll find the redundant edge using cycle detection algorithm.
        # 3. The edge that forms the cycle, that we encounter will be the redundant 
        #    edge only.
        
        N = len(edges)
        dsu = DSU(N)
        seen = set()

        for i, j in edges:
            # undirected edge: i <-> j

            if (i, j) in seen or (j, i) in seen:
                continue
            
            seen.add( (i, j) )

            if dsu.union(i, j):
                return [i, j]
            






