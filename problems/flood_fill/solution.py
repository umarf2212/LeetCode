class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def fill(image, sr, sc, color, startColor):
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
                return
            
            if image[sr][sc] != startColor or image[sr][sc] == color:
                return
        
            image[sr][sc] = color

            fill(image, sr-1, sc, color, startColor)
            fill(image, sr+1, sc, color, startColor)
            fill(image, sr, sc-1, color, startColor)
            fill(image, sr, sc+1, color, startColor)
        
        startColor = image[sr][sc]
        fill(image, sr, sc, color, startColor)
        return image
