class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        d = {}
        
        closestDist = float('inf')
        for i in range(len(points)):
            
            X, Y = points[i][0], points[i][1]
            
            if X==x or Y==y:
                
                dist = abs(X-x) + abs(Y-y)
                
                if dist < closestDist:
                    closestDist = dist
                    
                    if dist in d:
                        d[dist].append(i)
                    else:
                        d[dist] = [i]
        
        if not d: return -1
        res = d[min(d.keys())]
        return min(res)
        
        
                
