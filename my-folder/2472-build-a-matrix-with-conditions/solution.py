from collections import defaultdict

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        # [a, b] = a -> b = a before b in topo sort

        rowGraph = defaultdict(list)
        for a, b in rowConditions:
            rowGraph[a].append(b)
        
        colGraph = defaultdict(list)
        for a, b in colConditions:
            colGraph[a].append(b)

        def dfs(v, graph, vis, topoSort, recStack):
            if v in recStack:
                return False

            if v in vis:
                return True
            
            recStack.add(v)

            for u in graph[v]:
                if not dfs(u, graph, vis, topoSort, recStack):
                    return False
            
            recStack.remove(v)
            vis.add(v)
            topoSort.append(v)
            return True
        

        rowTopoSort = []
        rowVis = set()
        recStack = set()
        for i in range(1, k+1):
            if i not in rowVis:
                if not dfs(i, rowGraph, rowVis, rowTopoSort, recStack):
                    return []

        rowTopoSort = rowTopoSort[::-1]

        colTopoSort = []
        colVis = set()
        recStack = set()
        for i in range(1, k+1):
            if i not in colVis:
                if not dfs(i, colGraph, colVis, colTopoSort, recStack):
                    return []

        colTopoSort = colTopoSort[::-1]

        matrix = [[0] * k for _ in range(k)]

        numPositionInRows = {}
        for i in range(k):
            matrix[i][0] = rowTopoSort[i]
            numPositionInRows[rowTopoSort[i]] = i
        
        for j in range(k):
            num = colTopoSort[j]
            row = numPositionInRows[num]

            matrix[row][0] = 0
            matrix[row][j] = num

        return matrix

