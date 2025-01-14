class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        curElement = nums[0]
        count = 0

        for num in nums:
            if num == curElement:
                count += 1
            else:
                count -= 1

            if count == 0:
                curElement = num
                count = 1
        
        return curElement
