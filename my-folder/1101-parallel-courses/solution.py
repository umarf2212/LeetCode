from collections import defaultdict


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        """
        1.  First, find if there are any cycles. If there is a cycle
            in the graph, then it's not possible to take any course.

        2.  Min number of semesters? - basically longest path in the graph
        
        3.  There can be several longest paths and we don't know which starting
            node will give us the longest path.

        4.  So we try all possibilities - and of course since this is a DAG,
            there's optimal substructure and we can memoize results => DP
        """
        
        # Code below is a proof of concept for myself.
        # I am going to figure this out again.

        
        '''
            Create Graph
        '''
        graph = defaultdict(list)
        for prev, next in relations:
            graph[prev].append(next)

        vis = [0] * (n + 1)

        '''
            Check Cycle
        '''
        def dfsCheckCycle(v):
            vis[v] = 1

            for u in graph[v]:
                if vis[u] == 0:
                    dfsCheckCycle(u)

                elif vis[u] == 1:
                    isCycle[0] = True

            vis[v] = 2

        vis = [0] * (n + 1)
        isCycle = [False]
        for node in list(graph.keys()):
            dfsCheckCycle(node)

        if isCycle[0]:
            return -1

        '''
            Do Topological sorting
        '''
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(node)

        stack = []
        visited = set()
        for node in graph.keys():
            if node not in visited:
                dfs(node)

        top_order = stack[::-1]

        visitedLength = {}
        def dfsMaxPath(v):
            
            # we have already previously calculated max length,
            # which we do only once
            if v in visitedLength:
                return visitedLength[v]
            
            # min max-length this node will return to its neighbour 
            # is 1
            maxLength = 1
            for u in graph[v]:
                # find max length from v to u (and further)
                # + 1 for current node
                length = dfsMaxPath(u) + 1

                # compare and save max length so far 
                # from v to u (and further)
                maxLength = max(length, maxLength)
            
            # memoize the result once and for all, and return
            visitedLength[v] = maxLength
            return maxLength

        # calculate max length paths from 
        # every node as a starting point
        ans = -1
        for v in list(graph.keys()):
            ans = max(ans, dfsMaxPath(v))

        return ans

