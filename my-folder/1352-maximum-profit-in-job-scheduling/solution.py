from bisect import bisect_left
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        # 1. Sort the array by start times.
        # 2. At any job i, we either select it or skip it.
        # 3. If we choose to skip it, we move on to i+1 th job.
        # 4. If we choose to select it, then we add to the profit,
        #    and to find the next suitable job, we perform binary search 
        #    for end time of i'th job from i+1 to end of the array.
        # 5. We can observe that there is an optimal subtstructure and also
        #    the subproblems repeat, hence we can memoize them, so DP


        n = len(profit)

        # [startTime, endTime, profit]
        jobs = [[startTime[i], endTime[i], profit[i]] for i in range(n)]
        jobs.sort(key=lambda x:x[0])

        def findNextJob(jobs, position):
            curJobEnd = jobs[position][1]
            nextJob = len(jobs)

            start = position + 1
            end = len(jobs)-1
            while start <= end:
                mid = (start+end) // 2

                if jobs[mid][0] >= curJobEnd:
                    nextJob = mid
                    end = mid-1
                else:
                    start = mid+1
            
            return nextJob


        def maxProfit(jobs, position, memo):
            if position >= len(jobs):
                return 0

            if memo[position] != -1:
                return memo[position]

            
            nextJob = findNextJob(jobs, position)
            
            curMaxProfit = max(
                maxProfit(jobs, position+1, memo), 
                jobs[position][2] + maxProfit(jobs, nextJob, memo)
            )

            memo[position] = curMaxProfit
            return curMaxProfit
        
        memo = [-1] * len(jobs)
        return maxProfit(jobs, 0, memo)


            


