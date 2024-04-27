from collections import deque
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:

        X = x
        Y = y

        q = deque()
        q.append([0,0])

        vis = set()
        vis.add((0, 0))

        while q:
            x, y = q.popleft()

            if x+y == target:
                return True
            
            # X fills Y
            if x > Y-y:
                new_x = x - (Y-y)
                new_y = Y
            else:
                new_x = 0
                new_y = x + (Y-y)  

            if (new_x, new_y) not in vis:
                q.append( [new_x, new_y] )
                vis.add( (new_x, new_y) )

            # Y fills X
            if y > X-x:
                new_y = y - (X-x)
                new_x = X
            else:
                new_y = 0
                new_x = y + (X-x)
            
            if (new_x, new_y) not in vis:
                q.append( [new_x, new_y] )
                vis.add( (new_x, new_y) )

            # Completely empty either jug
            if (x, 0) not in vis:
                q.append( [x, 0] )
                vis.add( (x, 0) )
            
            if (0, y) not in vis:
                q.append( [0, y] )
                vis.add( (0, y) )

            # Complete fill either jug
            if (x, Y) not in vis:
                q.append( [x, Y] )
                vis.add( (x, Y) )
            
            if (X, y) not in vis:
                q.append( [X, y] )
                vis.add( (X, y) )

        return False


        
        #  x
        #  y
        
        # Operations we can do:
        # 1. Completely fill either jug
        # 2. Completely empty either jug
        # 3. Fill x to y
        # 4. Fill y to x

        # Filling (X)
        # Water content: x

        # Receiving
        # Capacity of the receiving jug: 
        # cy = (Y-y)

        # Capacity of Filling jug after filling receiving jug
        # x = x - (Y-y)

        # F (water) > R (capacity)
        # F (water) < R (capacity)


