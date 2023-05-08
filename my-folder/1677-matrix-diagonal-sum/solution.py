class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        i = 0
        j = 0
        Sum = 0
        while i < len(mat) and j < len(mat[0]):
            Sum += mat[i][j]
            i+=1
            j+=1
        
        i = 0
        j = len(mat[0])-1
        while i < len(mat) and j >= 0:
            Sum += mat[i][j]
            i+=1
            j-=1
        
        if len(mat) % 2 != 0:
            c = len(mat)//2
            Sum -= mat[c][c]
        
        return Sum

        

        # 0 0 0 0
        # 0 0 0 0
        # 0 0 0 0
        # 0 0 0 0

        # 0 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0 0
        
