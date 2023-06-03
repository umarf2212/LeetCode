class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def returnSingle(A):
            n = len(A)
            if len(A) % 2:
                return A[n//2]
            else:
                return ( A[(n//2)-1] + A[n//2] ) / 2
                
        if not nums1:
            return returnSingle(nums2)

        if not nums2:
            return returnSingle(nums1)

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1


        total = len(nums1) + len(nums2)
        half = total // 2

        l = 0
        r = len(nums1)
        while True:
            i = (l+r) // 2 # mid of nums1
            
            # mid of nums2, -2 because j itself is an index (so -1) 
            # and we subtract i from it so -1 from i as well 
            j = half - i - 2 

            left1 = nums1[i] if i >= 0 else float('-inf')
            right1 = nums1[i+1] if (i+1) < len(nums1) else float('inf')

            left2 = nums2[j] if j >= 0 else float('-inf')
            right2 = nums2[j+1] if (j+1) < len(nums2) else float('inf')

            # check if partition is correct
            if left1 <= right2 and left2 <= right1:
                # odd
                if total % 2:
                    return min(right1, right2)
                else:
                    #even
                    return (max(left1, left2) + min(right1, right2)) / 2
            
            elif left1 > right2:
                r = i-1
            else:
                l = i+1