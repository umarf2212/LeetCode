class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for row in range(len(mat)):
            res.append([sum(mat[row]), row])
        
        res.sort(key=lambda x: x[0], reverse=False)
        
        ans=[]
        for i in range(k):
            ans.append(res[i][1])
        
        return ans