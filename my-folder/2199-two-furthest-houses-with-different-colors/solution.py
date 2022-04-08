class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        maxDiff = float('-inf')
        for i in range(len(colors)):
            for j in range(i+1, len(colors)):
                
                if colors[i] != colors[j]:
                    maxDiff = max(j-i, maxDiff)
        
        return maxDiff
