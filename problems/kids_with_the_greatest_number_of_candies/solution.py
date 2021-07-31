class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        mx = max(candies)
        res = []
        
        for candy in candies:
            
            if candy+extraCandies >= mx:
                res.append(True)
            else:
                res.append(False)
            
        return res