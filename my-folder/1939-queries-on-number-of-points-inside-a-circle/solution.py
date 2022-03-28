class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        ans = []
        for query in queries:
            
            r = query[2]
            x1 = query[0]
            y1 = query[1]
            
            count = 0
            for point in points:
                x2 = point[0]
                y2 = point[1]
                
                ed = sqrt(((x2-x1)**2 + (y2-y1)**2))
                
                if ed <= r:
                    count += 1
            
            ans.append(count)
        
        return ans
