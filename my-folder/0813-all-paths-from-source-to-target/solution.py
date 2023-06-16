class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def traverse(graph, i, path, ans):

            # found the path from 0 to n-1
            if i >= len(graph)-1:
                ans.append(path[:])
                return
            
            for j in range(len(graph[i])):
                path.append(graph[i][j])
                traverse(graph, graph[i][j], path, ans)
                path.pop()
        
        ans = []
        path = [0]
        traverse(graph, 0, path, ans)
        return ans


