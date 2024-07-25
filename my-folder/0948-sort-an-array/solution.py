class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Merge Sort

        # 5 2 | 3 1

        def Merge(ar1, ar2):
            if not ar1: return ar2
            if not ar2: return ar1

            i = 0
            j = 0
            res = []
            while i < len(ar1) and j < len(ar2):
                if ar1[i] <= ar2[j]:
                    res.append(ar1[i])
                    i += 1
                else:
                    res.append(ar2[j])
                    j += 1
            
            if i < len(ar1):
                res += ar1[i:]
            
            if j < len(ar2):
                res += ar2[j:]
            
            return res
        
        def MergeSort(ar):
            if not ar or len(ar) == 1:
                return ar
            
            mid = len(ar) // 2

            left = MergeSort(ar[:mid])
            right = MergeSort(ar[mid:])

            return Merge(left, right)



        return MergeSort(nums)
