class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxLeft = []
        maxSoFar = -1
        for i in range(len(height)):
            maxSoFar = max(maxSoFar, height[i])
            maxLeft.append(maxSoFar)
        
        maxRight = []
        maxSoFar = -1
        for i in range(len(height)-1, -1, -1):
            maxSoFar = max(maxSoFar, height[i])
            maxRight.append(maxSoFar)
        maxRight = maxRight[::-1]
        
        ans = 0
        for i in range(len(height)):
            minHeight = min(maxLeft[i], maxRight[i])
            ans += minHeight - height[i]
        
        return ans




