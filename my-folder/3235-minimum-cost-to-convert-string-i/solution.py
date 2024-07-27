from collections import defaultdict
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        getLetterIndex = lambda letter: ord(letter) - 97
        
        m = len(original)
        graph = [[float('inf')] * 26 for _ in range(26)]
        
        # Cost of a self loop is 0
        for i in range(26):
            graph[i][i] = 0

        # v ----> u is a directed edge
        for i in range(m):
            v = getLetterIndex(original[i])
            u = getLetterIndex(changed[i])
            graph[v][u] = min(cost[i], graph[v][u])

        # Floyd Warshall Algorithm
        B = [[graph[i][j] for j in range(26)] for i in range(26)]
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if B[i][j] > B[i][k] + B[k][j]:
                        B[i][j] = B[i][k] + B[k][j]

        # Calculate the minimum costs
        n = len(source)
        res = 0
        for i in range(n):
            v = getLetterIndex(source[i])
            u = getLetterIndex(target[i])

            if B[v][u] == float('inf'):
                return -1
            
            res += B[v][u]

        return res

            

            
