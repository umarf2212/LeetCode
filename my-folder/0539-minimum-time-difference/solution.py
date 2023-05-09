class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        def convertToMinutes(time):
            time = list(map(int, time.split(":")))
            minutes = time[0] * 60
            minutes += time[1]
            return minutes

        ar = []
        for time in timePoints:
            minutes = convertToMinutes(time)
            ar.append(minutes)
        
        ar.sort()
        # print(ar)
        n = len(ar)
        minDiff = float('inf')
        for i in range(n-1):
            diff = (ar[i+1] - ar[i]) % 1440
            minDiff = min(minDiff, diff)
        
        # -1439 % 1440 = -1439+1440 => (a-b)%M = (a%M - b%M) + M
        diff = (ar[0]-ar[-1]) % 1440
        minDiff = min(minDiff, diff)

        return minDiff
