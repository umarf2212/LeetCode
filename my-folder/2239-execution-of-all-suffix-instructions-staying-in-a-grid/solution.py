class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        
        def checkBound(pos): 
            i, j = pos
            if i < 0 or i > n-1 or j < 0 or j > n-1 : return False
            return True
        
        res = []
        for i in range(len(s)):
            
            pos = [startPos[0], startPos[1]]
            totalMoves = 0
            move = i
            for move in range(i, len(s)):
                if s[move] == 'U':
                    pos[0] -= 1
                
                elif s[move] == 'D':
                    pos[0] += 1
                
                elif s[move] == 'L':
                    pos[1] -= 1
                
                elif s[move] == 'R':
                    pos[1] += 1
                
                if checkBound(pos):
                    totalMoves += 1
                else:
                    break
            
            res.append(totalMoves)
        
        return res
            
                
        
        
        
