from collections import defaultdict
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        
        parents = defaultdict(list)

        # edge: u -> v
        for u, v in edges:
            parents[v].append(u)
        
        def dfs(node, curNodeParents, vis):
            vis.add(node)

            for parent in parents[node]:
                if parent not in vis:
                    dfs(parent, curNodeParents, vis)
                curNodeParents.add(parent)

        
        res = []
        for i in range(n):
            curNodeParents = set()
            vis = set()
            dfs(i, curNodeParents, vis)
            res.append(sorted(curNodeParents))
        
        return res

