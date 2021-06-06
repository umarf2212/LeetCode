class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ = 0
        c = 0
        for r in range(len(mat)):
            summ += mat[r][c]
            c+=1
        
        c = len(mat)-1
        for r in range(len(mat)):
            summ += mat[r][c]
            c-=1
        
        return summ - mat[len(mat)//2][len(mat[0])//2] if len(mat)%2!=0 else summ
