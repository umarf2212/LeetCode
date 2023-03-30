class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        stack = []
        res = []
        revStack = [nums[i] for i in range(len(nums)-1,-1,-1)]
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            
            if not stack:
                while revStack and revStack[-1] <= nums[i]:
                    revStack.pop()

                if revStack:
                    res.append(revStack[-1])
                else:
                    res.append(-1)
            else:
                res.append(stack[-1])
            
            stack.append(nums[i])
        
        res = res[::-1]
        return res




        
        return res

