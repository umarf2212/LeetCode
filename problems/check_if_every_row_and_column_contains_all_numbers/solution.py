class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        n = len(matrix)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if matrix[i][j] not in rows[i]:
                    rows[i].add(matrix[i][j])
                else:
                    return False
                
                if matrix[i][j] not in cols[j]:
                    cols[j].add(matrix[i][j])
                else:
                    return False
        
        return True