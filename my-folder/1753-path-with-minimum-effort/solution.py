from heapq import heappop, heappush, heapify
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        # DIJKSTRA

        m, n = len(heights), len(heights[0])
        
        inf = float('inf')

        # (d, node) -> distance `d` from source to current `node`
        heap = [(0, 0, 0)]
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        dist = [[inf for _ in range(n)] for _ in range(m)]
        maxDiff = 0

        while heap:
            effort, i, j = heappop(heap)

            if i == m-1 and j == n-1:
                return effort

            if dist[i][j] == inf:
                dist[i][j] = effort

                for dx, dy in dirs:
                    new_i = dx + i
                    new_j = dy + j

                    if 0 <= new_i < m and 0 <= new_j < n:
                        newEffort = max(effort, abs(heights[new_i][new_j]-heights[i][j]))

                        if dist[new_i][new_j] == inf:
                            heappush(heap, (newEffort, new_i, new_j) )
        
        return maxDiff



                


