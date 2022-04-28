class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        ar = [nums[0]]
        for i in range(1, len(nums)):
            ar.append(ar[i-1] + nums[i])
        
        return ar