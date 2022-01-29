class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [nums[0]]
        runningSum = nums[0]
        for i in range(1, len(nums)):
            runningSum += nums[i]
            self.prefixSum.append(runningSum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0: 
            return self.prefixSum[right]
        return self.prefixSum[right] - self.prefixSum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# [-2,0,3,-5,2,-1] => [-2, -2, 1, -4, -2, -3]
