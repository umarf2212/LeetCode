class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        
        [[1,5], [3,6], [4,7]]

        nums.sort(key=lambda x:x[0])

        stack = [nums[0]]
        for i in range(1, len(nums)):
            if stack[-1][1] >= nums[i][0]:
                stack[-1][1] = max(nums[i][1], stack[-1][1])
            else:
                stack.append(nums[i])
        
        # print(stack)

        ans = 0
        for inter in stack:
            ans += inter[1]-inter[0] + 1
        
        return ans
