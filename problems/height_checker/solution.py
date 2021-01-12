class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        sortedHeights = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if abs(sortedHeights[i]-heights[i]) > 0:
                count += 1
        
        return count