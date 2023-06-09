class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        # 1 4 6 8 10
        # 1 5 11 19 29
        # 29 28 24 18 10
        # FOR 8: 7+4+2 + 2 = 15

        n = len(nums)

        prefix_left = [nums[0]]
        for i in range(1, n):
            prefix_left.append(prefix_left[-1]+nums[i])
        
        prefix_right = [nums[-1]]
        for i in range(n-2,-1,-1):
            prefix_right.append(prefix_right[-1]+nums[i])
        
        prefix_right = prefix_right[::-1]

        first = abs(prefix_right[1] - (nums[0] * (n-1)))
        res = [first]
        for i in range(1, len(nums)-1):
            left = abs(prefix_left[i-1] - (i * nums[i]))
            right = abs(prefix_right[i+1] - (nums[i] * (n-1-i)))
            res.append(abs(left)+abs(right))
        
        last = abs(prefix_left[-2] - (nums[-1] * (n-1)))
        res.append(last)

        return res