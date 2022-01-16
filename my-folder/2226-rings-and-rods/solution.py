class Solution:
    def countPoints(self, rings: str) -> int:
        
        rods = []
        for _ in range(10):
            rods.append([0,0,0])
        
        for i in range(0, len(rings), 2):
            c = rings[i]
            p = rings[i+1]
            
            if c == 'R':
                rods[int(p)][0] = 1
            elif c == 'G':
                rods[int(p)][1] = 1
            else:
                rods[int(p)][2] = 1
        
        # def allColors(rod):    
        #     if rod[0] > 0 and rod[1] > 0 and rod[2] > 0:
        #         return True
        #     return False

        return len(list(filter(lambda x: all(x), rods)))
