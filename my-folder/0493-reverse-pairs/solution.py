class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        
        # 1. Write normal merge sort
        # 2. Insert the reverse pair counting logic just before 
        #    the merge process.
        
        def merge(A, B):
            if not A: return B
            if not B: return A

            i = 0
            j = 0
            res = []
            while i < len(A) and j < len(B):
                if A[i] <= B[j]:
                    res.append(A[i])
                    i+=1
                else:
                    res.append(B[j])
                    j+=1

            if i < len(A): res += A[i:]
            
            if j < len(B): res += B[j:]
            
            return res

        def MergeSort(A, count):
            if len(A) <= 1:
                return A
            
            mid = len(A)//2

            left = MergeSort(A[:mid], count)
            right = MergeSort(A[mid:], count)

            # here we can leverage the fact that 
            # the elements of left half are smaller than 
            # that of right half

            i = 0
            j = 0
            while j < len(right):
                while i < len(left) and left[i] <= 2 * right[j]:
                    i += 1
                
                count[0] += len(left) - i
                j += 1


            return merge(left, right)
        
        count = [0]
        MergeSort(nums, count)

        return count[0]

