from collections import defaultdict
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        # 1, 2, 4
        # 1*2 + 1*4 = 2 + 4 = 6
        # 2*4 = 8
        # = 14

        # O(V + 2*E) = O(V+E)

        graph = defaultdict(list)
        for v, u in edges:
            graph[v].append(u)
            graph[u].append(v)

        
        def dfs(node, vis, graph, nodeCount):
            vis[node] = True

            nodeCount[0] += 1

            for neighbour in graph[node]:
                if not vis[neighbour]:
                    dfs(neighbour, vis, graph, nodeCount)
        
        # [1,2,3,4] [5,6] [7]
        
        CC = []
        vis = [False] * n
        nodeCount = [0]
        for node in range(n):
            if not vis[node]:
                dfs(node, vis, graph, nodeCount)
                CC.append(nodeCount[0])
                nodeCount = [0]
        
        # CC = [1,2,4]
        # ans = 0
        # for i in range(len(CC)):
        #     for j in range(i+1, len(CC)):
        #         ans += CC[i] * CC[j]

        ans = 0
        for i in range(len(CC)):
            cc = CC[i]

            ans += cc * (n-cc)
            n -= cc

        return ans



