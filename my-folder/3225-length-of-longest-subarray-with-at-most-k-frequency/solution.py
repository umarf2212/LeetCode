class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        ans = 0
        d = {}
        i = 0
        currLongest = 0
        for j in range(len(nums)):

            if nums[j] not in d:
                d[nums[j]] = 0
            d[nums[j]] += 1

            while i <= j and d[nums[j]] > k:
                d[nums[i]] -= 1
                currLongest -= 1
                i += 1

            currLongest += 1
            ans = max(ans, currLongest)

        return ans



