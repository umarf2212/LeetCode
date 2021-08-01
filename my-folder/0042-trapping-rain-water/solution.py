class Solution:
    def trap(self, height: List[int]) -> int:
        
        currMax = -1
        left = []
        for i in range(len(height)):
            currMax = max(currMax, height[i])
            left.append(currMax)
        
        currMax = -1
        right = []
        for i in range(len(height)-1, -1, -1):
            currMax = max(currMax, height[i])
            right.append(currMax)
        
        right = right[::-1]
        
        res = []
        
        for i in range(len(height)):
            level = min(left[i], right[i]) - height[i]
            res.append(level)
        
        return sum(res)
