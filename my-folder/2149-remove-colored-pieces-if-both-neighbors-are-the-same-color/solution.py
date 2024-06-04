class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        aliceTotalMoves = 0
        bobTotalMoves = 0
        for i in range(1, len(colors)-1):
            if colors[i-1] == 'A' and colors[i] == 'A' and colors[i+1] == 'A':
                aliceTotalMoves += 1
            
            if colors[i-1] == 'B' and colors[i] == 'B' and colors[i+1] == 'B':
                bobTotalMoves += 1

        # Since Alice goes first, Alice can only win if Alice has more number of 
        # moves than Bob. Otherwise, Bob will always win.

        if aliceTotalMoves > bobTotalMoves:
            return True
        return False




