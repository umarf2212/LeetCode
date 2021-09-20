class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        init_nums = nums.copy()
        nums.sort()
        d = {}
        
        # 1 2 2 3 8
        
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = i
        
        res = []
        for num in init_nums:
            res.append(d[num])
        
        
        return res