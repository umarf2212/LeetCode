class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = Counter(nums)
        
        for key, val in d.items():
            if val == 1:
                return key
