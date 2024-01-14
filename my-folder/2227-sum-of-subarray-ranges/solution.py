class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        nsl = []
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()    
            nsl.append(stack[-1] if stack else -1)
            stack.append(i)
    

        ngl = []
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()    
            ngl.append(stack[-1] if stack else -1)
            stack.append(i)
    
        nsr = []
        stack = []
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            nsr.append(stack[-1] if stack else -1)
            stack.append(i)

        nsr = nsr[::-1]
        
        ngr = []
        stack = []
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            ngr.append(stack[-1] if stack else -1)
            stack.append(i)

        ngr = ngr[::-1]

        Max = 0
        for k in range(len(nums)):
            left = k + 1 if ngl[k] == -1 else k - ngl[k]
            right = len(nums) - k if ngr[k] == -1 else ngr[k] - k
            Max += left * right * nums[k]
        
        Min = 0
        for k in range(len(nums)):
            left = k + 1 if nsl[k] == -1 else k - nsl[k]
            right = len(nums) - k if nsr[k] == -1 else nsr[k] - k
            Min += left * right * nums[k]
            
        return Max-Min
            

