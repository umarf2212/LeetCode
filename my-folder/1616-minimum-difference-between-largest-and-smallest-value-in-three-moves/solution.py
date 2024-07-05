class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        # [4,7,8,12,15,100]
        # [7,7,8,12,15,15]
        # now here, changing 100 to 15 means we technically remove it

        # and we have the choice to remove from either start or end
        # [4,7,8,12,15,100]
        # [7,7,8,12,15,100]
        # [8,8,8,12,15,100]
        # [12,12,12,12,15,100]

        # if array size is <= 4, then answer is just 0
        if len(nums) <= 4:
            return 0

        nums.sort()

        minDiff = nums[-1] - nums[0]

        # remove smallest three
        minDiff = min(minDiff, nums[-1] - nums[3] )

        # remove 2 smallest and 1 largest
        minDiff = min(minDiff, nums[-2] - nums[2] )

        # remove 1 smallest and 2 largest
        minDiff = min(minDiff, nums[-3] - nums[1] )

        # remove 3 largest
        minDiff = min(minDiff, nums[-4] - nums[0] )

        return minDiff




