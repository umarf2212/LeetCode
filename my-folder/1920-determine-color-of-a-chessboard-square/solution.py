class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        # x = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
        y = int(coordinates[1])
        
        if (ord(coordinates[0]) - 97) % 2 == 0:
            if y % 2 == 0:
                return True
            else:
                return False
        else:
            if y % 2 == 0:
                return False
            else:
                return True
