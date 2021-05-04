class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxNum = float('-inf')
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    maxNum = max(maxNum, (nums[i]-1)*(nums[j]-1))
                    
        return maxNum
        
