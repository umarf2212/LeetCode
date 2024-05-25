class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:

        # 1. We use BS to estimate a possible answer and converge it to the number
        #    closest to it in the matrix.
        # 2. We know that the median is definitely going to be in the range
        #    min(matrix) and max(matrix) so we start with these as lo and hi
        # 3. Now after guessing median each time, we find how many numbers are 
        #    smaller than this. For a median, the numbers smaller than it should be
        #    exactly (m*n) //2
        
        def findSmallerNos(row, median):
            # find largest number <= median
            if median < row[0]: 
                return 0
            if median > row[-1]: 
                return len(row)

            i = 0
            j = len(row)-1
            res = 0
            while i <= j:
                mid = (i+j) // 2

                if row[mid] <= median:
                    res = mid
                    i = mid + 1
                else:
                    j = mid - 1

            return res + 1


        m, n = len(grid), len(grid[0])

        lo = float('inf')
        hi = float('-inf')
        for row in grid:
            lo = min(lo, row[0])
            hi = max(hi, row[-1])

        ans = grid[0][0]
        minNumCount = (m*n) // 2 + 1
        while lo <= hi:
            median = (lo + hi) // 2

            smallerNos = 0
            for row in grid:
                smallerNos += findSmallerNos(row, median)
            
            if smallerNos >= minNumCount:
                ans = median
                hi = median - 1
            else:
                lo = median + 1
        
        return ans



        # [1,2,3,3,3, 4,4,5,6,7,8]
        # [1, 2, 3, 10, 100, 120, 130, 140]


