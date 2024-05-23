class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        '''
        difficulty = [2,4,6,8,10]
        profit =     [10,20,30,40,50]

        worker =     [4,5,6,7]
        '''

        jobs = list(zip(difficulty, profit))
        jobs.sort()
        worker.sort()

        i = 0
        bestProfit = 0
        ans = 0
        for skill in worker:
            while i < len(jobs) and skill >= jobs[i][0]:
                bestProfit = max(bestProfit, jobs[i][1])
                i += 1
            
            ans += bestProfit
        
        return ans


