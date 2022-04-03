class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        for i in range(1, len(nums)+1):
            res += list(combinations(nums, i))
        
        return res
