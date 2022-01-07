class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()
        
        ind = []
        for i, j in enumerate(nums):
            if j == target:
                ind.append(i)
                
        return ind