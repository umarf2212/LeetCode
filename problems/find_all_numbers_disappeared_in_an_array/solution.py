class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        d = {i:0 for i in range(1,len(nums)+1)}
        
        for i in nums: d[i] += 1
        
        return [i for i in d.keys() if d[i] == 0]