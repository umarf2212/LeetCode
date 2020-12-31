class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        Sum = n*(n+1)//2
        
        for i in nums:
            Sum -= i
        
        return Sum