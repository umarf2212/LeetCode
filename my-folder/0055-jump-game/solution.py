class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # 2 3 1 1 4

        # 2 3

        def canJumpFromPosition(pos):
            if dp[pos] != -1:
                return dp[pos]
            
            furthestJump = min(pos + nums[pos], len(nums)-1)

            for nextPos in range(pos+1, furthestJump+1):
                if canJumpFromPosition(nextPos):
                    dp[pos] = 1
                    return True
            
            dp[pos] = 0
            return False
        
        dp = [-1] * len(nums)
        dp[-1] = 1
    
        return canJumpFromPosition(0)


