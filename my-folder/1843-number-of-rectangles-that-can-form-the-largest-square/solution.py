class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        maxSide = float('-inf')
        d = {}
        for rect in rectangles:
            small_side = min(rect)
            
            if small_side in d:
                d[small_side] += 1
            else:
                d[small_side] = 1

        
        rects = 0
        maxSide = float('-inf')
        for side, count in d.items():
            if side > maxSide:
                maxSide = side
                rects = count
        
        return rects
