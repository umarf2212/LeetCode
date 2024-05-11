class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.trie
        for i in range(len(word)):
            if word[i] not in cur.children:
                cur.children[word[i]] = TrieNode()
            cur = cur.children[word[i]]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        return self.searchWord(word, 0, self.trie)
    
    def searchWord(self, word, i, curTrieNode):
        if i == len(word): return curTrieNode.isEnd

        if word[i] != '.' and word[i] not in curTrieNode.children:
            return False
        
        if word[i] in curTrieNode.children:
            return self.searchWord(word, i+1, curTrieNode.children[word[i]])
        
        elif word[i] == '.':
            curAns = False
            
            for ch in curTrieNode.children.keys():
                curAns = curAns or self.searchWord(word, i+1, curTrieNode.children[ch])
            
            return curAns

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
