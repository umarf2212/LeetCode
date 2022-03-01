class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        d = {}
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i-j not in d:
                    d[i-j] = [mat[i][j]]
                else:
                    d[i-j].append(mat[i][j])
        
        for ar in d.values():
            ar.sort(reverse=True)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = d[i-j].pop()
        
        
        return mat