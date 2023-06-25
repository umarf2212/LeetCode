class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [[set() for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == '.':
                    continue

                if num not in rows[i]:
                    rows[i].add(num)
                else:
                    return False
                
                if num not in cols[j]:
                    cols[j].add(num)
                else:
                    return False
                
                if num not in grids[i//3][j//3]:
                    grids[i//3][j//3].add(num)
                else:
                    return False
        
        return True


