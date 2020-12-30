class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1
        
        for num, count in d.items():
            if count >= len(nums)/2: return num
