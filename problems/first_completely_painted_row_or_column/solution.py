class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        m = len(mat)
        n = len(mat[0])

        d = {}
        for i in range(m):
            for j in range(n):
                d[mat[i][j]] = [i,j]

        rows = [0 for _ in range(m)]
        cols = [0 for _ in range(n)]
        for k in range(len(arr)):

            i, j = d[arr[k]]

            rows[i] += 1
            cols[j] += 1

            if rows[i] == n or cols[j] == m:
                return k