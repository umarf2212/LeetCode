class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        
        nums.sort()
        # print(nums)

        # 1 1 2 2 3 7

        moves = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                nextGreater = nums[i-1] + 1
                moves += nextGreater - nums[i]
                nums[i] = nextGreater
        
        # print(nums)
        return moves
