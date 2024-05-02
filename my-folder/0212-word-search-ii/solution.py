class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        trie = Trie()
        for word in words:
            trie.insert(word)

        m, n = len(board), len(board[0])

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def DFS(board, trieNode, i, j, curWord, ans):
            # if this function runs, 
            # then it implies trie[t]/board[i][j] exists

            if 'children' not in trieNode: return

            if trieNode['isEnd']:
                ans.add(curWord)
                # return

            for dx, dy in dirs:
                next_i = i + dx
                next_j = j + dy

                if 0 <= next_i < m and 0 <= next_j < n:
                    letter = board[next_i][next_j]

                    if letter in trieNode['children']:
                        curLetter = board[i][j]
                        board[i][j] = '#'
                        DFS(
                            board, 
                            trieNode['children'][letter], 
                            next_i, 
                            next_j, 
                            curWord + letter, 
                            ans
                        )
                        board[i][j] = curLetter

        ans = set()
        for i in range(m):
            for j in range(n):
                trieNode = trie.trie
                if board[i][j] in trieNode['children']:
                    DFS(
                        board, 
                        trieNode['children'][board[i][j]], 
                        i, 
                        j, 
                        board[i][j], 
                        ans
                    )
        
        return list(ans)


class Trie:
    def __init__(self):
        self.trie = {'children': {}, 'isEnd': False}

    def insert(self, word: str) -> None:
        root = self.trie
        for i in range(len(word)):
            ch = word[i]
            if ch not in root['children']:
                root['children'][ch] = {'children':{}, 'isEnd': False}

            if i == len(word)-1:
                root['children'][ch]['isEnd'] = True
            else:
                root = root['children'][ch]
