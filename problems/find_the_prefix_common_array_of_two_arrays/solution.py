class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        sa = set()
        sb  = set()
        res = []
        for i in range(len(A)):
            sa.add(A[i])            
            sb.add(B[i])
            
            res.append(len(sa.intersection(sb)))
        
        return res