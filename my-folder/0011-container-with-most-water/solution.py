class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Mainly a "Greedy" approach using Two Pointers
        
        # Area = l * b
        # = (j-i) * min(height[i], height[j])

        i = 0
        j = len(height)-1
        ans = 0
        while i < j:
            area = (j-i) * min(height[i], height[j])
            ans = max(ans, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return ans


