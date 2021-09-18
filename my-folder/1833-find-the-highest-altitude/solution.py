class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        # gain[i] -> gain in height
        # simply means add to previous height
        
        maxHeight = 0
        currHeight = 0
        for i in range(len(gain)):
            currHeight += gain[i]
            
            if currHeight > maxHeight:
                maxHeight = currHeight
            
        return maxHeight
