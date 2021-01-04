class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:       
        
        if len(flowerbed) == 1: return True if (flowerbed[0] == 0 or (flowerbed[0]==1 and n==0)) else False
        
        i = 0
        
        if flowerbed[0] == 0 and flowerbed[1]==0:
            flowerbed[0] = 1
            n -= 1

        while i <= len(flowerbed)-2:
            
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
            i += 1
        
        if flowerbed[i] == 0 and flowerbed[i-1]==0:
            flowerbed[0] = 1
            n -= 1
        
        if n>0:
            return False
        
        return True
