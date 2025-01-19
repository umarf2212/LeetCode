class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxLeft = []
        maxSoFar = -1
        for i in range(len(height)):
            maxSoFar = max(maxSoFar, height[i])
            maxLeft.append(maxSoFar)
        
        maxSoFar = -1
        for i in range(len(height)-1, -1, -1):
            maxSoFar = max(maxSoFar, height[i])
            maxLeft[i] = min(maxLeft[i], maxSoFar)
        
        ans = 0
        for i in range(len(height)):
            ans += maxLeft[i] - height[i]
        
        return ans




