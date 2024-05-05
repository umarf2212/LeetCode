class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        negatives = set()

        for num in nums:
            if num < 0:
                negatives.add(num)
        
        maxNum = -1
        res = -1
        for num in nums:
            if num > 0 and num > maxNum and -num in negatives:
                maxNum = num
                res = num
        
        return res
