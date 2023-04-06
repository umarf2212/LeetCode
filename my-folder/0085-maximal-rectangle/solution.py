class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        # 1. Make a Prefix Sum Matrix
        # 2. For every row, find max area in histogram using monotnic stack

        # initialise empty matrix
        prefix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        # fill up first row
        for i in range(len(matrix[0])):
            prefix[0][i] = int(matrix[0][i])
        
        # build prefix matrix
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                prefix[i][j] = (prefix[i-1][j] + int(matrix[i][j])) * int(matrix[i][j])
        
        # ar  = 4 3 6 10 8 5
        def maxRectangleInHistogram(ar):

            nsl = []
            stack = []
            for i in range(len(ar)):
                while stack and ar[stack[-1]] >= ar[i]:
                    stack.pop()
                
                if stack:
                    nsl.append(stack[-1])
                else:
                    nsl.append(-1)
                stack.append(i)
            
            nsr = []
            stack = []
            for i in range(len(ar)-1,-1,-1):
                while stack and ar[stack[-1]] >= ar[i]:
                    stack.pop()
                
                if stack:
                    nsr.append(stack[-1])
                else:
                    nsr.append(-1)
                stack.append(i)
            nsr = nsr[::-1]

            res = float('-inf')
            for i in range(len(ar)):

                if nsr[i] == -1 and nsl[i] == -1:
                    count = len(ar)
                
                elif nsr[i] != -1 and nsl[i] != -1:
                    count = (nsr[i] - nsl[i] - 1)
                
                elif nsl[i] == -1:
                    count = nsr[i]
                
                elif nsr[i] == -1:
                    count = (len(ar) - nsl[i] - 1)
                    
                res = max(res, count * ar[i])

            return res

        ans = 0
        for row in prefix:
            if any(row):
                ans = max(ans, 1)

            res = maxRectangleInHistogram(row)
            ans = max( ans, res )

    
        return ans



            # count of elements in the range = y-x+1
            # x = nsl + 1
            # y = nsr - 1
            
            # y-x+1 = (nsr-1) - (nsl+1) + 1
            # = nsr-1 -nsl
            # = nsr-nsl-1
