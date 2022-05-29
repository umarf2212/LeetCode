class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        xor = 0
        for num in range(len(nums)+1):
            xor ^= num
        
        for num in nums:
            xor ^= num
        
        return xor
