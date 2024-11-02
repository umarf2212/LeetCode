class Solution:
    def jump(self, nums: List[int]) -> int:
        

        # 2 3 1 1 4

        # curInd, steps

        def minSteps(curIndex):

            if curIndex >= len(nums)-1:
                return 0

            if nums[curIndex] == 0:
                return float('inf')
            
            if dp[curIndex] != -1:
                return dp[curIndex]
            
            ans = float('inf')
            for i in range(1, nums[curIndex]+1):
                nextInd = curIndex + i

                ans = min(ans, 1 + minSteps(nextInd))
            
            dp[curIndex] = ans
            
            return ans
        
        n = len(nums)
        dp = [-1] * n
        ans = minSteps(0)
        return ans


