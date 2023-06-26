class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:

        left = []
        S = set()
        for i in range(len(nums)):
            num = nums[i]
            if num not in S:
                S.add(num)
            
            left.append(len(S))
        
        right = []
        S = set()
        for i in range(len(nums)-1,-1,-1):
            num = nums[i]
            right.append(len(S))
            if num not in S:
                S.add(num)
        right = right[::-1]
        
        res = []
        for i in range(len(left)):
            res.append(left[i]-right[i])

        return res
