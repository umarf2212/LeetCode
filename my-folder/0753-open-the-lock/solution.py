from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        vis = set()

        for deadend in deadends:
            vis.add(tuple([int(i) for i in deadend]))
        
        if (0,0,0,0) in vis:
            return -1
        
        q = deque([ [(0,0,0,0), 0] ])
        vis.add((0,0,0,0))

        target = tuple([int(i) for i in target])

        while q:

            cur, moves = q.popleft()

            if cur == target:
                return moves

            for i in range(4):
                nextMove = list(cur)
                nextMove[i] = 0 if nextMove[i] == 9 else nextMove[i]+1
                nextMove = tuple(nextMove)

                if nextMove not in vis:
                    vis.add(nextMove)
                    q.append([nextMove, moves+1])
            
            for i in range(4):
                nextMove = list(cur)
                nextMove[i] = 9 if nextMove[i] == 0 else nextMove[i]-1
                nextMove = tuple(nextMove)
                
                if nextMove not in vis:
                    vis.add(nextMove)
                    q.append([nextMove, moves+1])

        return -1



