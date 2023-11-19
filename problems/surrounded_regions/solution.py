class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        A = board

        m, n = len(A), len(A[0])

        def inBounds(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            return True
        
        # It's simply about borders. Any O's on border are not to be captured,
        # along with all other O's connected to them, hence DFS on them.

        # All other O's - capture em all up.

        def dfs(i, j):
            if not inBounds(i, j) or A[i][j] != 'O':
                return
            
            A[i][j] = 'E'

            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        for i in range(m):
            if A[i][0] == 'O': dfs(i, 0)
            if A[i][n-1] == 'O': dfs(i, n-1)
        
        for j in range(n):
            if A[0][j] == 'O': dfs(0, j)
            if A[m-1][j] == 'O': dfs(m-1, j)

        for i in range(m):
            for j in range(n):
                if A[i][j] == 'O':
                    A[i][j] = 'X'

                elif A[i][j] == 'E':
                    A[i][j] = 'O'
