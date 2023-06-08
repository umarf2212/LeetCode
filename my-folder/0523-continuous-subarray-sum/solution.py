class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        d = {}
        curSum = 0
        for i in range(len(nums)):
            curSum += nums[i]
            mod = curSum % k

            if mod == 0 and i > 0:
                return True

            if mod not in d:
                d[mod] = i

            elif i - d[mod] > 1:
                return True
        
        return False
