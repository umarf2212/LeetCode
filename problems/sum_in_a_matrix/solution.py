class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:

        for row in nums:
            row.sort(reverse=True)
        
        score = 0
        for j in range(len(nums[0])):
            Max = float('-inf')
            for i in range(len(nums)):
                Max = max(Max, nums[i][j])

            score += Max
        
        nums = [[]]

        return score            
