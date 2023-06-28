class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])

        visited = [[0 for _ in range(n)] for _ in range(m)]

        # O(len(word))
        def backtrack(board, word, i, j, k, visited):
            if k == len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j]:
                return False

            visited[i][j] = 1
            if word[k] == board[i][j]:
                
                if backtrack(board, word, i+1, j, k+1, visited):
                    return True

                if backtrack(board, word, i, j+1, k+1, visited):
                    return True

                if backtrack(board, word, i-1, j, k+1, visited):
                    return True

                if backtrack(board, word, i, j-1, k+1, visited):
                    return True
            visited[i][j] = 0


        #O(mn)
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if backtrack(board, word, i, j, 0, visited):
                        return True
        return False
