class Solution:
    def trap(self, height: List[int]) -> int:
        
        # Nearest max to the Left and Nearst Max to the Right
        # and get minimum of maxes on both sides for max water level 
        # minus the height of the current building

        curMax = -1
        left = []
        for i in range(len(height)):
            curMax = max(height[i], curMax)
            left.append(curMax)
        
        curMax = -1
        right = []
        for i in range(len(height)-1,-1,-1):
            curMax = max(height[i], curMax)
            right.append(curMax)
        right = right[::-1]

        res = 0
        for i in range(len(height)):
            res += min(left[i], right[i]) - height[i]
        
        return res
