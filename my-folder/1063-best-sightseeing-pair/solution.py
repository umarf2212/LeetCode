class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        # score => values[i] + values[j] + i - j
        # (values[i] + i) + (values[j] - j)

        n = len(values)
        leftSum = []
        for i in range(n):
            cur = values[i] + i
            leftSum.append( values[i] + i )
        

        rightSum = []
        for j in range(n):
            rightSum.append( values[j] - j )

        # print(leftSum)
        # print(rightSum)

        curMax = leftSum[0]
        for i in range(n):
            if leftSum[i] < curMax:
                leftSum[i] = curMax
            else:
                curMax = leftSum[i]

        curMax = rightSum[-1]
        for i in range(n-1,-1,-1):
            if rightSum[i] < curMax:
                rightSum[i] = curMax
            else:
                curMax = rightSum[i]

        # print(leftSum)
        # print(rightSum)

        ans = -1
        for i in range(n-1):
            curSum = leftSum[i] + rightSum[i+1]
            if curSum > ans:
                ans = curSum

        return ans


