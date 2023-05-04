class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        # 5 4 1 3 8 9 2 1 7 6 2
        # sum = 28
        # k = 3

        def canSplitArray(nums, maxSum, k):
            count = 1
            curSum = 0
            for i in range(len(nums)):
                curSum += nums[i]
                if curSum > maxSum:
                    curSum = nums[i]
                    count += 1
            
            if count > k:
                return False
            return True

        lo = max(nums)
        hi = sum(nums)
        ans = float('inf')
        while lo <= hi:

            mid = (lo+hi)//2

            if (canSplitArray(nums, mid, k)):
                hi = mid-1
                ans = mid
            else:
                lo = mid+1
        
        return lo
