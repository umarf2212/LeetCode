class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def MergeSort(ar):
            if len(ar) == 1:
                return ar
                
            mid = len(ar)//2
            return merge(MergeSort(ar[:mid]), MergeSort(ar[mid:]))
        
        def merge(A, B):
            if not A: return B
            if not B: return A

            i = 0
            j = 0
            res = []
            while i < len(A) and j < len(B):
                if A[i] <= B[j]:
                    res.append(A[i])
                    i += 1
                else:
                    res.append(B[j])
                    j += 1
            
            if i < len(A):
                res += A[i:]
            
            if j < len(B):
                res += B[j:]
            
            return res
        
        return MergeSort(nums)

