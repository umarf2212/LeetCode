class Solution:
    
    def fill(self, image, r, c, startPixel, newColor):
        if (r < 0 or r >= len(image)) or (c < 0 or c >= len(image[0])): return False
        
        if image[r][c] == startPixel:
            image[r][c] = newColor
        
            self.fill(image, r-1, c, startPixel, newColor)
            self.fill(image, r+1, c, startPixel, newColor)
            self.fill(image, r, c-1, startPixel, newColor)
            self.fill(image, r, c+1, startPixel, newColor)
        
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        if image[sr][sc] == newColor: return image
        
        self.fill(image, sr, sc, image[sr][sc], newColor)
        return image