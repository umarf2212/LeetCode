class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        nums.sort()

        n = len(nums)
        roots = {}

        for i in range(n):
            sq = nums[i] * nums[i]
            roots[sq] = [i, 1]

            if nums[i] in roots:
                roots[sq] = [i, roots[nums[i]][1] + 1]


        ans = 1
        for item in roots.values():
            ans = max(ans, item[1])

        if ans == 1:    
            return -1

        return ans
