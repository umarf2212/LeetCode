class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:

        mins = []
        maxs = []
        for i, ar in enumerate(arrays):
            mins.append([ar[0], i])
            maxs.append([ar[-1], i])

        mins.sort(key=lambda x:x[0])
        maxs.sort(key=lambda x:x[0], reverse=True)


        if mins[0][1] != maxs[0][1]:
            return maxs[0][0] - mins[0][0]
        else:
            return max( maxs[0][0]-mins[1][0], maxs[1][0]-mins[0][0] )

