class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        nsl = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                nsl.append(stack[-1])
            else:
                nsl.append(-1)

            stack.append(i)
    
        stack = []
        nsr = []
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                nsr.append(stack[-1])
            else:
                nsr.append(-1)
            
            stack.append(i)

        nsr = nsr[::-1]

        # [y-x+1 is number of bars]
        # (NSR[i]-1) - (NSL[i]+1) + 1 
        # NSR[i] - NSL[i] - 1

        ans = float('-inf')
        for i in range(len(heights)):
            
            if nsl[i] == -1 and nsr[i] == -1:
                cur = heights[i] * len(heights)            
            elif nsl[i] != -1 and nsr[i] != -1:
                cur = (nsr[i]-nsl[i]-1) * heights[i]
            
            elif nsl[i] == -1:
                cur = nsr[i] * heights[i]
            
            elif nsr[i] == -1:
                cur = (len(heights) - nsl[i] - 1) * heights[i]

            ans = max(ans, cur)
        
        return ans
