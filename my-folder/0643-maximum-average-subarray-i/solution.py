class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        maxSum = sum(nums[:k])
        sumSoFar = maxSum
        
        i=0
        while i+k < len(nums):
            sumSoFar = sumSoFar-nums[i]+nums[i+k]
            maxSum = max(maxSum, sumSoFar)
            i+=1
        
        return maxSum/k
