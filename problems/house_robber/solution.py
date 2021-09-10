class Solution:
    def rob(self, nums: List[int]) -> int:
        
        '''
            1 2 3 6 4    8 7 3 2
                    i-1  i
            
            M(i) = max( nums[i] + M(i-2) , M(i-1) )
            M(0) = nums[0]
            M(1) = max(nums[0], nums[1])
            
        '''
        if len(nums) == 1: return nums[0]
        
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max( dp[i-1] , nums[i] + dp[i-2] )
            
        return dp[len(nums)-1]