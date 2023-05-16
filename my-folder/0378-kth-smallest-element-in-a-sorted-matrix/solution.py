class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        # O(m+n) = O(2n) = O(n)
        def countNums(matrix, num):
            n = len(matrix)
            count = 0
            i = 0
            j = n-1
            for i in range(n):
                while j >= 0 and matrix[i][j] > num:
                    j -= 1
                count += j+1
            return count

        # O( log( max-min ) )
        lo = matrix[0][0]
        hi = matrix[-1][-1]
        while lo <= hi:
            mid = (lo+hi) // 2

            if countNums(matrix, mid) >= k:
                hi = mid-1
            else:
                lo = mid+1

        # For every Binary Search routine log(max-min), the function 
        # countNums will run which itself is O(n)
        # Hence TC = O( nlog(max-min) )
        
        return lo
