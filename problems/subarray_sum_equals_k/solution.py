class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # 1 5 -2 4 -1 1 2 8
        
        # 1 6 4 8 7 8 10 18

        curSum = 0
        d = {}
        res = 0
        for i in range(len(nums)):
            curSum += nums[i]

            if curSum == k:
                res += 1

            diff = curSum - k

            if diff in d:
                res += d[diff]
            
            if curSum not in d:
                d[curSum] = 1
            else:
                d[curSum] += 1
        
        return res