class Solution:
    
    def rotate(self, mat):
        newMat = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                newMat[c][r] = mat[r][c]
        
        return newMat[::-1]
    
    def compare(self, mat1, mat2):
        for r in range(len(mat1)):
            for c in range(len(mat1[0])):
                if mat1[r][c] != mat2[r][c]:
                    return False
        return True
    
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        ar = [self.compare(mat, target)]
        
        for _ in range(3):
            mat = self.rotate(mat)
            ar.append(self.compare(mat, target))
        
        return any(ar)