from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        # 1. bombs[i] = [x, y, r]
        n = len(bombs)

        def distance(x1, y1, x2, y2):
            return (x2-x1)**2 + (y2-y1)**2

        graph = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i == j: continue

                x1, y1, r1 = bombs[i]
                x2, y2, _ = bombs[j]

                dist = distance(x1, y1, x2, y2)

                if dist <= r1**2:
                    graph[i].append(j)
        
        def dfs(v, count):
            vis.add(v)
            count[0] += 1

            for u in graph[v]:
                if u not in vis:
                    dfs(u, count)
        
        ans = 0
        for i in range(n):
            vis = set()
            count = [0]
            dfs(i, count)
            ans = max(ans, count[0])
        

        return ans


        







