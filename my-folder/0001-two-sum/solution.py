class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        for i in range(len(nums)):
            num = nums[i]

            if target - num in d:
                return [i, d[target-num]]
            
            d[num] = i
