class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        i = len(nums)
        while i > 1:
            newNums = []
            for j in range(len(nums)-1):
                newNums.append((nums[j]+nums[j+1]) % 10)
            
            nums = newNums
            i -= 1
        
        return nums[0]

