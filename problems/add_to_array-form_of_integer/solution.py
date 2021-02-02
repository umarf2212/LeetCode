class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        # a = int(''.join(A))
        return [i for i in str(int(''.join([str(j) for j in A]))+K)]