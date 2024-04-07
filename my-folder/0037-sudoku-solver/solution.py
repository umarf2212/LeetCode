class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        A = board
        # change input to proper matrix
        for i in range(len(A)):
            A[i] = list(A[i])

        # initialize hashsets
        rowSet = [set() for _ in range(9)]
        colSet = [set() for _ in range(9)]
        boxSet = [[set() for _ in range(3)] for _ in range(3)]
        
        # fill up the hashsets with initial given data
        for i in range(9):
            for j in range(9):
                if A[i][j] != '.':
                    rowSet[i].add(A[i][j])
                    colSet[j].add(A[i][j])
                    boxSet[i//3][j//3].add(A[i][j])
        
        def findEmpty(A):
            for r in range(9):
                for c in range(9):
                    if A[r][c] == '.':
                        return r, c
            return -1, -1

        def isSafe(num, r, c):
            if num in rowSet[r] or num in colSet[c] or num in boxSet[r//3][c//3]:
                return False
            return True
        
        def traverse(A):
            r, c =  findEmpty(A)

            if r == -1 and c == -1:
                A = [int(''.join(row)) for row in A]
                return True

            for num in range(1, 10):
                num = str(num)
                if isSafe(num, r, c):
                    A[r][c] = num
                    rowSet[r].add(num)
                    colSet[c].add(num)
                    boxSet[r//3][c//3].add(num)

                    if traverse(A):
                        return True

                    A[r][c] = '.'
                    rowSet[r].remove(num)
                    colSet[c].remove(num)
                    boxSet[r//3][c//3].remove(num)

        traverse(A)
