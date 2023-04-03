class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        smallerThanTarget = 0
        targetCount = 0
        for i in range(len(nums)):
            if nums[i] < target:
                smallerThanTarget += 1
            
            elif nums[i] == target:
                targetCount += 1
        
        return [i for i in range(smallerThanTarget, smallerThanTarget+targetCount)]
