class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        s = set(nums)
        
        for num in nums:
            if original in s:
                original *= 2
            else:
                s.add(num)
        
        return original