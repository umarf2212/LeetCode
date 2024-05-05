from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        ind = [0] * numCourses

        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)
            ind[u] += 1
        
        q = deque()
        for i in range(len(ind)):
            if ind[i] == 0:
                q.append(i)
        
        topo = []
        count = 0
        while q:
            v = q.popleft()

            topo.append(v)

            for u in adj[v]:
                ind[u] -= 1

                if ind[u] == 0:
                    q.append(u)
            
            count += 1
    
        # if there is a cycle
        if count != numCourses:
            return []
        
        return topo


    


