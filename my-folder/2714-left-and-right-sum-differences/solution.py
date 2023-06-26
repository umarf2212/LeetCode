class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:


        n = len(nums)

        leftSum = [0]
        Sum = nums[0]
        for i in range(1, n):
            leftSum.append(Sum)
            Sum += nums[i]
        
        rightSum = [0]
        Sum = nums[-1]
        for i in range(n-2,-1,-1):
            rightSum.append(Sum)
            Sum += nums[i]
        
        rightSum = rightSum[::-1]
        
        res = []
        for i in range(n):
            res.append(abs(leftSum[i]-rightSum[i]))
        
        return res
