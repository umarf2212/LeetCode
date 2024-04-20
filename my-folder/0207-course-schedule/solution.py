from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if len(prerequisites) == 0:
            return True
        
        adj = defaultdict(list)
        ind = [0] * numCourses
        for edge in prerequisites:
            # j --> i
            i = edge[0]
            j = edge[1]
            adj[j].append(i)
            ind[i] += 1
        

        q = deque()
        # keep in mind we have to consider all courses 
        # from 0 to n. Prerequisites may not necessarily 
        # contain all the courses. Only the dependent ones.
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)

        visited = 0
        while q:
            v = q.popleft()
            visited += 1

            for u in adj[v]:
                ind[u] -= 1
                if ind[u] == 0:
                    q.append(u)
        
        return visited == numCourses

        
        
